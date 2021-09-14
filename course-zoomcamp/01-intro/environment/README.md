# Setup Environment using Docker 

The following guide is for facilitating an environment using [Docker](https://www.docker.com/). 

## What do I gain by setting up a docker container? 

- A portable and isolated environment that you can update and destroy once you are done. 
- You can re-use it for any ML Applications that you might want to develop without the worry of the OS you are running on. 


### Ok, I'm sold, what should I do now? 

## Pre-Requirements

- Install Docker based on the OS you are using. 
 
    Reference: [Docker - Get Started](https://www.docker.com/get-started)

## Build your docker image

Once you have Docker installed, Follow the next steps to build your image. 

1. Enter the environment folder.

Execute the following command from the root folder of your repo: **mlbookcamp-code**

```
cd ./course-zoomcamp/01-intro/environment
```

2. Build your image

Note: Ensure you have a Dockerfile and environment.yml in the folder you are in.

Build the image by passing as tag the name of your image. In the example below is called: **ml-zoomcamp**

```
docker build -t ml-zoomcamp .
```

3. Check your image is built successfully 

```
docker images ml-zoomcamp
```

Output example: 
```
REPOSITORY    TAG       IMAGE ID       CREATED      SIZE
ml-zoomcamp   latest    79985d76ae2b   2 days ago   5.92GB
```

4. Run your image with Jupyter 

**Note**: after you have built your image, go back to the root folder of the repo, so that, when you run  your container all notebooks will be available.

```
docker run -it -p 8888:8888 -v $PWD:/data ml-zoomcamp
```

Copy the link from the output and you will see jupyter opening and ready to use. 

Output example: 
```
[I 20:34:00.048 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 20:34:00.050 NotebookApp]

Copy/paste this URL into your browser when you connect for the first time,to login with a token:

http://localhost:8888/?token=05f0940c0afa6ba641c3244efd930b891039ff5f6c7a621f
```

## Using your docker image

Every time you want to use your docker image, simply run the command: 

```
docker run -it -p 8888:8888 -v $PWD:/data ml-zoomcamp
``` 

This will open jupyter in your browser. 

## How to add more libraries or update a version? 

Follow the next steps.

1. Go to the [environments.yml](./environment.yml)

You should see a list as follows: 

```
name: ml-zoomcamp
channels:
  - conda-forge
dependencies:
  - python=3.8
  - jupyter
  - numpy
  - pandas
```

2. Edit the list of dependencies with the version you would like to use or add/remove libraries as you need.

3. Build your docker image again by following step 2 - Build your docker image.