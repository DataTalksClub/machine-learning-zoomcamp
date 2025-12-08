# Model Deployment with Kubernetes and ONNX

* Video: https://www.youtube.com/live/c_CzCsCnWoU?si=fgQ56JwunM3NoiWm

In this workshop, we will explore deploying ML models using Kubernetes, building upon concepts from:

- [Module 5 - FastAPI deployment](../../05-deployment/)
- [Module 9 - Serverless and ONNX](../../09-serverless/)

Instead of deploying to AWS Lambda, we'll deploy to a local Kubernetes cluster using Kind (Kubernetes in Docker), making it accessible and cost-free for learners.


We will not cover theory in detail. For that, refer to the old content of [ML Zoomcamp module 10](../).


## Plan

The plan for the workshop:

- Setting up local Kubernetes with Kind
- Building a FastAPI service for ONNX model inference
- Containerizing the service with Docker
- Deploying to Kubernetes
- Scaling with Horizontal Pod Autoscaler
- Health checks and resource management

## Prerequisites

- Docker
- Basic understanding of Python and ML models
- Familiarity with FastAPI

## Environment Setup

First, let's install the required tools.

### Install kubectl

kubectl is the Kubernetes command-line tool.

**Windows (with Chocolatey):**

```bash
choco install kubernetes-cli
```

**macOS:**

```bash
brew install kubectl
```

**Linux:**

```bash
cd 

mkdir bin && cd bin

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl

cd

export PATH="${PATH}:${HOME}/bin"
# add it to .bashrc

which kubectl
```

Verify installation:
```bash
kubectl version --client
```

### Install Kind

Kind (Kubernetes in Docker) allows you to run Kubernetes clusters locally using Docker containers.

**Windows (with Chocolatey):**
```bash
choco install kind
```

**macOS:**
```bash
brew install kind
```

**Linux:**
```bash
curl -Lo ${HOME}/bin/kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ${HOME}/bin/kind
```

Verify installation:
```bash
kind version
```

### Install uv

```bash
pip install uv
```

### Create a Kind Cluster

Let's create a local Kubernetes cluster:

```bash
kind create cluster --name mlzoomcamp
```

This will:

- Create a single-node Kubernetes cluster
- Configure kubectl to use this cluster
- Take a few minutes on first run (downloads images)

Verify the cluster is running:

```bash
kubectl cluster-info
kubectl get nodes
```

You should see one node in "Ready" status.

## Model Preparation

We will use a pre-trained PyTorch model that classifies clothing items. The model has already been converted to ONNX format.

Download the ONNX model:

```bash
mkdir service 
cd service

wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing_classifier_mobilenet_v2_latest.onnx -O clothing-model.onnx
```

**Note:** If you want to learn how to convert PyTorch models to ONNX, check the [mlzoomcamp-serverless workshop](../mlzoomcamp-serverless/README.md#aws-lambda-pytorch-models).

The model predicts one of 10 clothing categories from an image URL.

## Building the FastAPI Service

We will create a FastAPI application that serves the ONNX model for inference.

The service structure is similar to what we built in the [FastAPI workshop](../mlzoomcamp-fastapi-uv/), but adapted for ONNX models.

First, initialize the project:

```bash
# cd service
uv init
rm main.py
```

Add dependencies:

```bash
uv add fastapi uvicorn onnxruntime keras-image-helper numpy
```

Now create the FastAPI application. See [`service/app.py`](service/app.py).


**Key points:**

- Uses ONNX Runtime for inference
- Custom PyTorch-style preprocessing function (the PyTorch model requires specific normalization)
- `keras-image-helper` for image preprocessing
- Pydantic models for input/output validation
- Health endpoint for Kubernetes health checks


### Testing Locally

Run the service:

```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

Open http://localhost:8080/docs to see the API documentation.

Create a test script [`service/test.py`](service/test.py):

```python
import requests

url = 'http://localhost:8080/predict'

request = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

response = requests.post(url, json=request)
result = response.json()

print(f"Top prediction: {result['top_class']} ({result['top_probability']:.2%})")
print(f"\nAll predictions:")
for cls, prob in result['predictions'].items():
    print(f"  {cls:12s}: {prob:.2%}")
```

Run the test:

```bash
uv run python test.py
```

You should see predictions for the clothing item.

**Alternative: Test with curl**

```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "http://bit.ly/mlbookcamp-pants"}'
```

**Windows (PowerShell):**
```powershell
curl.exe -X POST http://localhost:8080/predict `
  -H "Content-Type: application/json" `
  -d '{\"url\": \"http://bit.ly/mlbookcamp-pants\"}'
```

Or check the health endpoint:

```bash
curl http://localhost:8080/health
```


## Docker Containerization

Now let's containerize our application.

Create [`service/Dockerfile`](service/Dockerfile).

Build the image:

```bash
docker build -t clothing-classifier:v1 .
```

Test the container locally:

```bash
docker run -it --rm -p 8080:8080 clothing-classifier:v1
```

In another terminal, run the test script:

```bash
uv run python test.py
```

Or test with curl:

```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"url": "http://bit.ly/mlbookcamp-pants"}'
```

## Loading Image to Kind

Kind clusters run in Docker, so they can't access images from your local Docker daemon by default. We need to load the image into Kind.

```bash
kind load docker-image clothing-classifier:v1 --name mlzoomcamp
```


## Kubernetes Deployment

Now let's deploy our service to Kubernetes.

### Understanding Kubernetes Resources

- **Pod**: The smallest deployable unit in Kubernetes (one or more containers)
- **Deployment**: Manages a set of identical Pods, handles updates and scaling
- **Service**: Exposes Pods to network traffic
- **HPA (Horizontal Pod Autoscaler)**: Automatically scales Pods based on metrics

### Create Deployment Manifest

Let's create a folder for all the config files:

```bash
mkdir k8s
cd k8s
```

Create [`k8s/deployment.yaml`](k8s/deployment.yaml)

**Key configuration:**
- `replicas: 2` - Run 2 copies of our service
- `imagePullPolicy: Never` - Use local image (don't pull from registry)
- `resources` - Memory and CPU limits/requests
- `livenessProbe` - Restart container if unhealthy
- `readinessProbe` - Only send traffic when ready

Deploy it:

```bash
kubectl apply -f deployment.yaml
```

Check the deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl describe deployment clothing-classifier
```

View logs:

```bash
kubectl logs -l app=clothing-classifier --tail=20
```

### Create Service Manifest

Create [`k8s/service.yaml`](k8s/service.yaml).

**Key configuration:**
- `type: NodePort` - Expose on a static port on each node
- `nodePort: 30080` - Accessible on port 30080 from host
- `selector` - Routes traffic to Pods with matching labels

Deploy it:

```bash
kubectl apply -f k8s/service.yaml
```

Check the service:

```bash
kubectl get services
kubectl describe service clothing-classifier
```

### Testing the Deployed Service

With NodePort, the service is accessible on `localhost:30080`:


Check the health endpoint:

```bash
curl http://localhost:30080/health
```

Our kind cluster is not configured for `NodePort`, so it won't work. We don't really need this for testing things locally, so let's just use a quick fix: Use `kubectl port-forward`. 

```bash
kubectl port-forward service/clothing-classifier 30080:8080
```

Now it's accessible on port 30080

```bash
curl http://localhost:30080/health
```

When we deploy to EKS or some other Kubernetes in the cloud, it won't be a problem - there Elastic Load Balancer will solve this problem. 


## Horizontal Pod Autoscaling

Kubernetes can automatically scale your application based on CPU or memory usage.

TODO descibe what HPA is and give a simple example

First, we need metrics-server for HPA to work. Install it in kubectl:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

TODO describe what mestrics-server is 

For Kind, we need to patch metrics-server to work without TLS:

```bash
kubectl patch -n kube-system deployment metrics-server --type=json -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
```

TODO describe why

Wait for metrics-server to be ready:

```bash
kubectl get deployment metrics-server -n kube-system
```

We should see something like that:

```
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
metrics-server   1/1     1            1           72s
```

Now create [`k8s/hpa.yaml`](k8s/hpa.yaml).

**Configuration:**

- Scale between 2 and 10 replicas
- Target 50% CPU utilization
- Automatically adds/removes Pods based on load

Deploy HPA:

```bash
kubectl apply -f hpa.yaml
```

Check HPA status:

```bash
kubectl get hpa
kubectl describe hpa clothing-classifier-hpa
```

### Testing Autoscaling

Generate load to trigger autoscaling. You can use a simple load test (see [`load_test.py`](load_test.py))

First, check that you can access the endpoint:

```bash
curl http://localhost:30080/health
```

Run the test:

```bash
uv run python load_test.py
``` 

While running the load test, watch the HPA in another terminal:

```bash
kubectl get hpa -w
```

You should see the number of replicas increase as CPU usage rises.

Check Pods:

```bash
kubectl get pods -w
```

## Managing the Deployment

### Updating the Application

If you make changes to your code:

1. Rebuild the image with a new tag:
```bash
docker build -t clothing-classifier:v2 .
```

2. Load to Kind:
```bash
kind load docker-image clothing-classifier:v2 --name mlzoomcamp
```

3. Update deployment:
```bash
kubectl set image deployment/clothing-classifier clothing-classifier=clothing-classifier:v2
```

Or update the YAML file and apply:
```bash
kubectl apply -f k8s/deployment.yaml
```

Watch the rollout:
```bash
kubectl rollout status deployment/clothing-classifier
```

### Scaling Manually

Scale to 5 replicas:
```bash
kubectl scale deployment clothing-classifier --replicas=5
```

### Viewing Logs

All Pods:
```bash
kubectl logs -l app=clothing-classifier --tail=50
```

Specific Pod:
```bash
kubectl logs <pod-name>
```

Follow logs:
```bash
kubectl logs -f -l app=clothing-classifier
```

### Debugging

Describe resources:
```bash
kubectl describe deployment clothing-classifier
kubectl describe pod <pod-name>
kubectl describe service clothing-classifier
```

Get events:
```bash
kubectl get events --sort-by='.lastTimestamp'
```

Execute commands in a Pod:
```bash
kubectl exec -it <pod-name> -- /bin/bash
```


## Cleanup

Delete the deployment and service:

```bash
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
kubectl delete -f k8s/hpa.yaml
```

Or delete everything at once:

```bash
kubectl delete all -l app=clothing-classifier
kubectl delete hpa clothing-classifier-hpa
```

Delete the Kind cluster:

```bash
kind delete cluster --name mlzoomcamp
```

## Summary

We covered:

1. **Local Kubernetes Setup**
   - Installing kubectl and Kind
   - Creating a local Kubernetes cluster
   - Basic kubectl commands

2. **ONNX Model Deployment**
   - Using pre-converted ONNX model for inference
   - Building FastAPI service with ONNX Runtime
   - Containerizing the application with Docker

3. **Kubernetes Deployment**
   - Creating Deployment manifests
   - Exposing services with NodePort
   - Health checks (liveness and readiness probes)
   - Resource limits and requests

4. **Scaling and Management**
   - Horizontal Pod Autoscaling based on CPU
   - Manual scaling
   - Rolling updates
   - Debugging and logging

**Next Steps:**

- Deploy to cloud Kubernetes (EKS, GKE, AKS)
- Use Ingress for advanced routing
- Implement monitoring with Prometheus and Grafana
- Explore MLOps tools like Kubeflow or Seldon Core
- Learn about service mesh (Istio, Linkerd)
- Implement CI/CD pipelines for automated deployments

**Differences from AWS Lambda:**

Kubernetes gives you more control and flexibility, but requires more management. It's ideal for production workloads that need consistent performance and complex orchestration.
