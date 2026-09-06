---
video_url: "https://www.youtube.com/watch?v=89jxeddZtC0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
---
# Deploying to EKS

In this lesson we move everything from our local kind cluster to the
cloud: we create an Elastic Kubernetes Service (EKS) cluster on Amazon
using the command line, publish our Docker images to ECR, apply the same
Kubernetes configuration files to the remote cluster, and configure
kubectl to work with it.

To create the cluster and manage it on EKS we'll use a CLI tool
[eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html).

One thing to note before starting: EKS is not part of the Amazon Web
Services Free Tier, so running the cluster costs money. Remember to
delete it when you're done.

## Creating the EKS cluster

In the `kube-config` folder we create the EKS config file,
`eks-config.yaml`. We give the cluster a name and a region, and define
the node group - the machines our pods will run on. For our case we need
only one node group (CPU):

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: mlzoomcamp-eks
  region: eu-west-1

nodeGroups:
  - name: ng-m5-xlarge
    instanceType: m5.xlarge
    desiredCapacity: 1
```

Creating the cluster takes a while - eksctl provisions the control plane
and boots the worker nodes:

```bash
eksctl create cluster -f eks-config.yaml
```

After it finishes, eksctl has also configured kubectl to talk to the new
cluster - `kubectl get nodes` shows the node coming from EKS.

## Publishing the images to ECR

Our Docker images live only on our machine, so far kind could pull them
from the local Docker daemon. A cluster in the cloud can't - we need to
publish the images somewhere the EKS nodes can pull from. That place is
ECR, the Amazon container registry.

First we create a repository for our images:

```bash
aws ecr create-repository --repository-name mlzoomcamp-images
```

Then we tag our local images with remote names and push them. In a bash
script:

```bash
# Registry URI
ACCOUNT_ID=387546586013
REGION=eu-west-1
REGISTRY_NAME=mlzoomcamp-images
PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY_NAME}

# Tag local docker images to remote tag
GATEWAY_LOCAL=zoomcamp-10-gateway:002 # gateway service
GATEWAY_REMOTE=${PREFIX}:clothing-model-gateway-002 # notice the ':' is replaced with '-' before 002
docker tag ${GATEWAY_LOCAL} ${GATEWAY_REMOTE}

MODEL_LOCAL=zoomcamp-10-model:xception-v4-001 # tf-serving model
MODEL_REMOTE=${PREFIX}:clothing-model-xception-v4-001 # same thing ':' is replaced with '-' before xception
docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}

# Login to ecr and push tagged docker images
$(aws ecr get-login --no-include-email)

# Push tagged docker images
docker push ${MODEL_REMOTE}
docker push ${GATEWAY_REMOTE}
```

ECR doesn't allow the `:` character in the tag part after the repository
name, which is why we replace it with `-`.

Finally we get the URI of these images with `echo ${MODEL_REMOTE}` and
`echo ${GATEWAY_REMOTE}`, and put them into `model-deployment.yaml` and
`gateway-deployment.yaml` respectively. For example, the model deployment
now uses the ECR image:

```yaml
spec:
  containers:
  - name: tf-serving-clothing-model
    image: 387546586013.dkr.ecr.eu-west-1.amazonaws.com/mlzoomcamp-images:zoomcamp-10-model-xception-v4-001
```

## Applying the configuration to the remote cluster

The same Kubernetes configuration files we used with kind work on EKS as
they are. We apply all of them:

```bash
kubectl apply -f model-deployment.yaml
kubectl apply -f model-service.yaml
kubectl apply -f gateway-deployment.yaml
kubectl apply -f gateway-service.yaml
```

Testing the deployment pods and services should give us predictions - the
gateway still reaches the model through
`tf-serving-clothing-model.default.svc.cluster.local:8500`, now on the
EKS network.

Executing `kubectl get service` gives us the external address of the
gateway's load balancer. We add it to `test.py` as the access URL for
predictions, for example:

```python
url = 'http://a3399eXXXX-5180XXXX.eu-west-1.elb.amazonaws.com/predict'
```

## Deleting the cluster

When you're done experimenting, delete the remote cluster so it stops
costing money:

```bash
eksctl delete cluster --name mlzoomcamp-eks
```

## Notes

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>
