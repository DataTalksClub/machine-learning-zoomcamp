
## 7.6 Bento Production Deployment

<a href="https://www.youtube.com/watch?v=aF-TfJXQX-w&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-7-06.jpg"></a>
 
## Links
* [Installing the AWS command line interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Amazon ECS](https://aws.amazon.com/ecs/)

## Instructor Clarifications
**Fargate is actually not in the free tier**

As configured in the video with 0.25 CPUs it will cost $0.01 per hour.
In addition, any images stored in ECR over 500MB will cost $0.10/GB per month 


## Notes

In this lession we'll deploy our model to Amazon ECS (Elastic Container Service). This service makes it easy for us to deploy and scale our containerized applications.

First thing we need is to get our model tag that we want to used to create docker image, or we can simply run `bentoml build` to get the latest tag. Then we will create docker container using `bentoml containerize model:tag --platform=linux/amd64`, the option --plaform=linux/amd64 will prevent us from getting any deployment issues on ECS.

Once the container is built, we need to setup ECR container repository where we can store the docker image:

- Create Identity and Access Management (IAM) user.
- Get the Security credentials (if don't have already):
  - From top right drop-down menu > Security credentials > Access keys
- Install AWS CLI.
- Connect AWS with local machine by running `aws configure` command to provide credentials.
- Create Amazon Elastic Container Registry (ECR):
  - Click Get Started > General settings > Create repository
- Authenticate and push docker image to ECR:
  - Click on the repo name > View push commands > follow the instructions and tag the docker image built with bentoml (skip the step 2 because we have already built the docker image).

Now we need to setup Amazon Elastic Container Service (ECS) to run our docker image:

- Search and click Elastic Container Service in the search bar.
- Create and Configure Cluster:
  - Click Create Cluster > Networking only (CPU only) > follow the instructions.
- Create Task Definitions:
  - Click Create new Task Definition > FARGRATE > Task memory (0.5GB), Task CPU (0.25 vCPU) > Add container (follow instructions and paste the image URI of ECR repo into the *Image* section, also increase the *Soft limit* to 256 and set *Port mappings* to 3000) > create task
- Run the Task:
  - From ECS dashboard > Clusters > select the cluster we just created > Tasks > Run new Task > follow instructions (also select *Launch type* FARGATE, *Operating system family* Linux, *Security groups* set custom tcp to 3000) > create Task

Once the Task is running we can click on it to see all of the information including the *Public IP* which we can entry in the browser to access the service.

If we want to share the model or saving it to cloud, we can do so with `bentoml export model:tag path_to_store/modelname.bento` command and with this we can save the model in a local or push the model on save in the cloud (e.g., on Amazon S3 bucket). Beside the native .bento format, we can also save the model in `('tar')`, `tar.gz ('gz')`, `tar.xz ('xz')`, `tar.bz2 ('bz2')`, and `zip`.

In addition we can also import bentoml models from cloud or other sources using `bentoml import path_to_access_/model_name.bento`.

**References**:

- [ML Bookcamp article to Get Started with AWS and Creating IAM ROle](https://mlbookcamp.com/article/aws)
- [AWS CLI installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

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

## Additional Issue Support
* Thanks for watching! Depending on your local setup, we do find issues from time to time. If you run into anything strange
we have a big community of BentoML users who would be happy to receive issue feedback: 
[BentoML slack community](https://l.bentoml.com/join-slack-mlzoomcamp). And if you're around shoot me a direct
message and say hi! 😃 

~Tim


## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 7: Production-Ready Machine Learning (Bento ML)](./)
* Previous: [High-Performance Serving](05-high-performance.md)
* Next: [(Optional) Advanced Example: Deploying Stable Diffusion Model](07-stable-diffusion.md)