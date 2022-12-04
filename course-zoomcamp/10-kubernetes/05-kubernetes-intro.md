
## 10.5 Introduction to Kubernetes

<a href="https://www.youtube.com/watch?v=UjVkpszDzgk&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-10-05.jpg"></a>
 

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-10-kubernetes)


## Notes

Add notes from the video (PRs are welcome)

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


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 10: Kubernetes and TensorFlow Serving](./)
* Previous: [Running everything locally with Docker-compose](04-docker-compose.md)
* Next: [Deploying a simple service to Kubernetes](06-kubernetes-simple-service.md)
