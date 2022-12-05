## 10.8 Deploying to EKS

<a href="https://www.youtube.com/watch?v=89jxeddZtC0&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-10-08.jpg"></a>

In the section we'll create Elastic Kubernetes Service (EKS) cluster on Amazon using cli, publishing the image to ECR and configure kubectl.

To create cluster and manage on EKS we'll use a cli tool `eksctl` which can be downloaded from [here](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html). And next we'll follow these steps:

- In the `kube-config` folder create eks config file `eks-config.yaml`:
  - ```yaml
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
      name: mlzoomcamp-eks
      region: ap-south-1

    nodeGroups: # for our case, we need only one node group (CPU)
      - name: ng-m5-xlarge
        instanceType: m5.xlarge
        desiredCapacity: 1
    ```
  - Create eks cluster: `eksctl create cluster -f eks-config.yaml`
- Publish local docker images to ECR:
  - Create aws ecr repository for eks cluster: `aws ecr create-repository --repository-name mlzoomcamp-images`
  - Bash commands to run in the teminal to push docker images to ecr repository:
    - ```bash
      # Registry URI
      ACCOUNT_ID=22782589
      REGION=ap-south-123
      REGISTRY_NAME=mlzoomcamp-images
      PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY_NAME}

      # Tag local docker images to remote tag
      GATEWAY_LOCAL=clothing-model-gateway:002 # gateway service
      GATEWAY_REMOTE=${PREFIX}:clothing-model-gateway-002 # notice the ':' is replaced with '-' before 002
      docker tag ${GATEWAY_LOCAL} ${GATEWAY_REMOTE}

      MODEL_LOCAL=clothing-model:xception-v4-001 # tf-serving model
      MODEL_REMOTE=${PREFIX}:clothing-model-xception-v4-001 # same thing ':' is replaced with '-' before xception
      docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}


      # Push tagged docker images
      docker push ${MODEL_REMOTE}
      docker push ${GATEWAY_REMOTE}
      ```
    - Login to ecr and push images: `$(aws ecr get-login --no-include-email)`, first push the model and then gateway remote image.
    - Get the uri of these images `echo ${MODEL_REMOTE}` and `echo ${GATEWAY_REMOTE}` and add them to `model-deployment.yaml` and `gate-deployment.yaml` respectively.
  - Apply all the yaml config files to remote node coming from eks (`kubectl get nodes`):
    - `kubectl apply -f model-deployment.yaml`
    - `kubectl apply -f model-service.yaml`
    - `kubectl apply -f gateway-deployment.yaml`
    - `kubectl apply -f gateway-service.yaml`
      - Testing the deployment pods and services should give us predictions.
  - Executing `kubectl get service` should give us the *external port* address which need to add in the `test.py` as access url for predictions (e.g., `url = 'http://a3399e***-5180***.ap-south-123.elb.amazonaws.com/predict'`).

- To delete the remote cluster: `eksctl delete cluster --name mlzoomcamp-eks`


## Notes

Add notes from the video (PRs are welcome)


<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 10: Kubernetes and TensorFlow Serving](./)
* Previous: [Deploying TensorFlow models to Kubernetes](07-kubernetes-tf-serving.md)
* Next: [Summary](09-summary.md)