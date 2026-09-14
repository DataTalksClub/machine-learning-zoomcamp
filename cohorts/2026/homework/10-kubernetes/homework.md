## Homework 10: Kubernetes and Model Serving

In this homework we deploy the same lead-scoring API from Homework 5 to a
local Kubernetes cluster created with `kind`. The 2026 release fixes the image
tag, application port, service selector, resource requests, and HPA bounds.
The checked-in manifests are executable starting points; there are no
references to the 2025 directory or to a prior model.

## Build the 2026 image

From the repository root:

```bash
cd cohorts/2026/homework/05-deployment
docker build -t zoomcamp-model:2026-hw10 .
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw10
```

In another terminal, verify the API:

```bash
python q6_test.py
```

The request uses a complete 2026 lead record and the response schema is:

```json
{
  "conversion_probability": 0.0,
  "conversion": false
}
```

The probability is deterministic for the checked-in artifact. Stop the local
container before creating the Kubernetes service, then move to the manifest
directory:

```bash
cd ../10-kubernetes
```

## Question 1 — local container schema

Run the container and `q6_test.py`. Report `conversion_probability` rounded to
three decimal places. The grader accepts an absolute error of `0.005`.

## Installing `kubectl` and `kind`

Install `kubectl` and `kind` using their official installation instructions if
they are not already available. Record their versions in your notes. Version
checks are setup diagnostics, not graded answers, because the client binaries
are maintained independently of this homework.

## Question 2 — environment check

Run:

```bash
kind --version
kubectl version --client
```

Record the output. Do not submit a version-specific multiple-choice answer.

## Create a cluster

Use a named cluster so that the commands do not accidentally target an
unrelated local cluster:

```bash
kind create cluster --name mlzoomcamp-2026
kubectl cluster-info --context kind-mlzoomcamp-2026
```

## Question 3 — Kubernetes primitives

What is the smallest deployable computing unit that Kubernetes creates and
manages?

- Node
- Pod
- Deployment
- Service

## Question 4 — default service type

List the services in the new cluster:

```bash
kubectl get services --context kind-mlzoomcamp-2026
```

What is the `TYPE` of the service named `kubernetes`?

- `NodePort`
- `ClusterIP`
- `ExternalName`
- `LoadBalancer`

This is a property of the named kind cluster's default service, not of an
external cloud provider.

## Question 5 — load the local image

Kind nodes cannot automatically see images in the host Docker daemon. Load the
exact image into the named cluster:

```bash
kind load docker-image zoomcamp-model:2026-hw10 \
  --name mlzoomcamp-2026
```

Which command performs this operation?

- `kind create cluster`
- `kind build node-image`
- `kind load docker-image`
- `kubectl apply`

## Question 6 — deploy the API

Apply the checked-in deployment:

```bash
kubectl apply -f deployment.yaml --context kind-mlzoomcamp-2026
kubectl rollout status deployment/subscription --context kind-mlzoomcamp-2026
kubectl get pods --context kind-mlzoomcamp-2026
```

The deployment uses image `zoomcamp-model:2026-hw10`, listens on container port
`9696`, and has a readiness probe on `/health`.

What value is used for the container port?

- `80`
- `8080`
- `9000`
- `9696`

## Question 7 — expose the deployment

Apply the checked-in service:

```bash
kubectl apply -f service.yaml --context kind-mlzoomcamp-2026
kubectl get service subscription --context kind-mlzoomcamp-2026
```

The service deliberately uses `ClusterIP`, which works on every kind install;
we will access it with port forwarding rather than relying on a cloud
`LoadBalancer` implementation.

Which selector value routes traffic to the deployment?

- `app: api`
- `app: subscription`
- `app: lead-scoring`
- `app: zoomcamp-model`

Forward the service port and run the same client:

```bash
kubectl port-forward service/subscription 9696:80 \
  --context kind-mlzoomcamp-2026
python ../05-deployment/q6_test.py
```

The probability should match Question 1 within `0.005`.

## Autoscaling

The supplied `hpa.yaml` uses the current `autoscaling/v2` API and declares a
fixed range of one to three replicas:

```bash
kubectl apply -f hpa.yaml --context kind-mlzoomcamp-2026
kubectl get hpa subscription-hpa --context kind-mlzoomcamp-2026
```

If the CPU target is `unknown`, the cluster needs a metrics-server installation
and the HPA cannot yet make a scaling decision. This is an infrastructure
status, not an answer to submit.

## Question 8 — HPA configuration

What `maxReplicas` is declared in `hpa.yaml`?

- `1`
- `2`
- `3`
- `4`

This checks the version-controlled configuration instead of asking how many
replicas happened to appear during an uncontrolled load test. As an optional
experiment, run a loop that posts requests to the forwarded service and watch
`kubectl get hpa subscription-hpa --watch`; the observed replica count is not
graded.

## Clean up

When finished:

```bash
kind delete cluster --name mlzoomcamp-2026
```

## Submit the results

Submit the results here:
<https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw10>.

Numeric probabilities use the tolerance
stated above; environment versions and live HPA observations are not graded.
