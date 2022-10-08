## 5.6 Environment management: Docker

<a href="https://www.youtube.com/watch?v=wAtyYZ6zvAs&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-06.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Installing Docker
To isolate more our project file from our system machine, there is an option named Docker. With Docker you are able to pack all your project is a system that you want and run it in any system machine. For example if you want Ubuntu 20.4 you can have it in a mac or windows machine or other operating systems. <br>
To get started with Docker for the churn prediction project you can follow the instructions below.

### Ubuntu 

```bash
sudo apt-get install docker.io
```

To run docker without `sudo`, follow [this instruction](https://docs.docker.com/engine/install/linux-postinstall/).

### Windows

To install the Docker you can just follow the instruction by Andrew Lock in this link: https://andrewlock.net/installing-docker-desktop-for-windows/

### MacOS

Please send a PR!


## Notes

- Once our project was packed in a Docker container, we're able to run our project on any machine.
- First we have to make a Docker image. In Docker image file there are settings and dependecies we have in our project. To find Docker images that you need you can simply search the [Docker](https://hub.docker.com/search?type=image) website.

Here a Dockerfile (There should be no comments in Dockerfile, so remove the comments when you copy)

```docker
# First install the python 3.8, the slim version have less size
FROM python:3.8.12-slim

# Install pipenv library in Docker 
RUN pip install pipenv

# we have created a directory in Docker named app and we're using it as work directory 
WORKDIR /app                                                                

# Copy the Pip files into our working derectory 
COPY ["Pipfile", "Pipfile.lock", "./"]

# install the pipenv dependecies we had from the project and deploy them 
RUN pipenv install --deploy --system

# Copy any python files and the model we had to the working directory of Docker 
COPY ["*.py", "churn-model.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 9696

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "churn_serving:app"]
```

If we don't put the last line `ENTRYPOINT`, we will be in a python shell.
Note that for the entrypoint, we put our commands in doble quotes.

After creating the Dockerfile, we need to build it:

```bash
docker build -t churn-prediction .
```

- We use the `-t` flag for specifying the tag name "churn-prediction"

To run it,  execute the command below:

```bash
docker run -it -p 9696:9696 churn-prediction:latest
```

Here we use 

- `-it` in order to the Docker run from terminal and shows the result
- `-p` to map the 9696 port of the Docker to 9696 port of our machine. (first 9696 is the port number of our machine and the last one is Docker container port.)


At last you've deployed your prediction app inside a Docker continer. Congratulations 🥳



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
* [Session 5: Deploying Machine Learning Models](./)
* Previous: [Python virtual environment: Pipenv](05-pipenv.md)
* Next: [Deployment to the cloud: AWS Elastic Beanstalk (optional)](07-aws-eb.md)
