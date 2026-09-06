---
video_url: "https://www.youtube.com/watch?v=UjVkpszDzgk&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"
---
# Introduction to Kubernetes

In this lesson we look at the main concepts of Kubernetes: what a cluster
consists of, how pods, deployments and services relate to each other, and
how Kubernetes scales an application up and down depending on the load.

Kubernetes, also known as K8s, is an open-source system for automating
the deployment, scaling, and management of containerized applications.
For us the key word is scaling: to scale up means adding more instances of
our application when the load increases, and removing instances when the
load decreases. Kubernetes does this automatically.

## Anatomy of a Kubernetes cluster

Imagine we have a Kubernetes cluster. Within this cluster, there are
nodes - servers or computers running the processes. Kubernetes itself
doesn't create these machines; it uses the machines we give it, and on
each node it can run multiple containers.

On these nodes we find pods. A pod is a container that runs a specific
image, with allocated resources like RAM and CPU. One container is one
pod.

Pods are typically grouped into deployments. All pods in a deployment
share the same Docker image and configuration - think of a deployment as
a set of identical workers, ready to process requests. For example, our
gateway service can be structured as a deployment: several identical
gateway pods, each downloading images, resizing them and talking to the
model.

## Services

When there are several pods serving the same application, someone needs to
route the request to the right pod. That's what services do: a service is
an entry point that forwards requests to the pods that belong to it.

There are two kinds:

- An external service, of type `LoadBalancer`, is accessible from outside
  the cluster. Our gateway service is an example: it's the visible entry
  point for clients.
- An internal service, of type `ClusterIP`, is accessible only within the
  cluster. Our tf-model service is an example: it manages communication
  with the model-serving pods, and only the gateway needs to reach it.

## How a request flows

Putting it together:

1. When a user uploads an image on the website, the request first reaches
   the gateway service.
2. The gateway service routes the request to one of the available gateway
   pods, distributing the traffic evenly - load balancing.
3. The gateway pod pre-processes the image and forwards the request to
   the model service.
4. The model service routes the request to one of the pods in the
   tf-serving deployment.
5. The prediction is made and sent back to the user, following the same
   path in reverse.

At the front of the cluster there's an entry point called `Ingress`. It
directs user traffic coming into the cluster to the appropriate external
services.

## Scaling with Kubernetes

To handle multiple users simultaneously, Kubernetes can launch additional
pods:

- As traffic increases, Kubernetes automatically scales the deployment up
  - it adds more pods from the same template.
- When traffic decreases, it scales down to save resources.
- This dynamic scaling is managed by the Horizontal Pod Autoscaler (HPA):
  it allocates resources depending on demand.
- If the existing nodes are overwhelmed, Kubernetes can even request the
  creation of new nodes to handle the extra load.

All of this - the deployments, the services, the ingress, the scaling
rules - is described in Kubernetes configuration files, written in YAML.
In the next lesson we write such configuration ourselves and deploy a
simple service to a local Kubernetes cluster.

## Materials

- [Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-10-kubernetes)

## Notes

* kubernetes is open source system for automating deployment scaling and management of containerized applications
* to scale up = add more instances of our application
* add more instances when load increases and remove instances when load decreases
* kubernetes cluster consists of nodes (running machines, servers)
* each node can have multiple container
* one container = one pod
* grouping pods according to type of docker image
* routing the request to the pods
* external (visible, i.e. entry point) service/client vs internal service/client
* HPA horizontal pod autoscaler = allocating resources depending on demand
* Ingress
* kubernetes configuration

<table>
   <tr>
      <td>⚠️</td>
      <td>
         The notes are written by the community. <br>
         If you see an error here, please create a PR with a fix.
      </td>
   </tr>
</table>
