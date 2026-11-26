## 10. Kubernetes and TensorFlow Serving

Note: these materials are partly outdated, which
is why we recorded a workshop that updates this module.
You will find the materials in the [workshop/](workshop/) folder

You don't need to watch any of the module videos. But lessons 10.5 and 10.8 may still be useful.


- 10.1 [Overview](01-overview.md) - Introduce the serving architecture of a TensorFlow Serving model behind a Flask gateway, deployed on Kubernetes.
- 10.2 [TensorFlow Serving](02-tensorflow-serving.md) - Convert the Keras model to SavedModel, run TensorFlow Serving in Docker, and call it over gRPC from a notebook.
- 10.3 [Creating a pre-processing service](03-preprocessing.md) - Convert the notebook into a Flask gateway that prepares requests and drops TensorFlow for a protobuf helper.
- 10.4 [Running everything locally with Docker-compose](04-docker-compose.md) - Build separate Docker images for the model and gateway, then connect them with Docker Compose on one network.
- 10.5 [Introduction to Kubernetes](05-kubernetes-intro.md) - Explain Kubernetes nodes, pods, deployments, services, autoscaling and ingress at a conceptual level.
- 10.6 [Deploying a simple service to Kubernetes](06-kubernetes-simple-service.md) - Deploy a Flask ping service to a local kind cluster with a deployment, a LoadBalancer service and MetalLB.
- 10.7 [Deploying TensorFlow models to Kubernetes](07-kubernetes-tf-serving.md) - Deploy the TF-Serving model and the gateway to kind with deployments, ClusterIP and LoadBalancer services.
- 10.8 [Deploying to EKS](08-eks.md) - Create an EKS cluster with eksctl, push images to ECR, and apply the same Kubernetes configs to the cloud.
- 10.9 [Summary](09-summary.md) - Recap the two-tier TensorFlow Serving and gateway architecture, the local and EKS deployment, and alternatives.
- 10.10 [Explore more](10-explore-more.md) - List other local Kubernetes tools and managed cloud Kubernetes services, and suggest deploying other models.


## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Alvaro Navas' Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/10_kubernetes.md)
* [Notes from Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/10-kubernetes)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/10_kubernetes/Summary_Session_10.md)
* [Notes from Revathy Ramalingam](https://github.com/RevathyRamalingam/machineLearning/tree/main/10-kubernetes/README.md)
* Add your notes here
