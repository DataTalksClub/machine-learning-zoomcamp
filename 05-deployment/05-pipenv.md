## 5.5 Python virtual environment: Pipenv

<a href="https://www.youtube.com/watch?v=BMXh8JGROHM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-05.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Notes
In this session we're going to make virtual environments for our project. So Let's start this session by getting to know what is a virtual environment and how to make it.
- Every time we're running a file from a directory we're using the executive files from a global directory. When we install python on our machine the executable files that are able to run our codes will go to somewhere like _/home/username/python/bin/_. The pip command, for example, may go to _/home/username/python/bin/pip_.
- Sometimes the versions of libraries conflict (the project may not run or get into massive errors). For example, we have an old project that uses sklearn library with the version of 0.24.1 and now we want to run it using sklearn version 1.0.0. We may get into errors because of the version conflict.
   - To solve the conflict we can make virtual environments. A virtual environment is an operation that can separate the libraries installed in our system and the libraries with specified version we want our project to run with. There are a lot of ways to create virtual environments. One way we are going to use is a library named pipenv.
   - pipenv is a library that can create a virutal environment. To install this library just use the classic method ```pip install pipenv```.
   - After installing pipenv we must install the libraries we want for our project in the new virtual environment. It's really easy, Just use the command pipenv instead of pip. ```pipenv install numpy scikit-learn==0.24.1 flask```. With this command we installed the libraries we want for our project.
   - Note that using the pipenv command we made two files named _Pipfile_ and _Pipfile.lock_. If we look at these files closely we can see that in Pipfile the libraries we installed are named. If we specified the library name, it's also specified in Pipfile.
   - In _Pipfile.lock_ we can see that each library with its installed version is named and a hash file is there to reproduce if we move the environment to another machine.
   - If we want to run the project in another machine, we can easily install the libraries we want with the command ```pipenv install```. This command will look into _Pipfile_ and _Pipfile.lock_ to install the libraries with specified version.
   - After installing the required libraries we can run the project in the virtual environment with ```pipenv shell``` command. This will go to the virtual environment's shell and then any command we execute will use the virtual environment's libraries. Typing `gunicorn --bind localhost:9696 predict:app` can run the web service. However, if we prefer to use only one command to run the application in our environment, we just have to type: `pipenv run gunicorn --bind localhost:9696 predict:app`.
- Installing and using the libraries such as gunicorn is the same as the last session.
- Until here we made a virtual environment for our libraries with a required specified version. To seperate this environment more, such as making gunicorn be able to run in windows machines we need another way. The other way is using Docker. Docker allows us to seperate everything more than before and make any project able to run on any machine that supports Docker smoothly.
- In the next session we'll go in detail of how Docker works and how to use it.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/13/ml-zoomcamp-2023-deploying-machine-learning-models-part-5/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 5: Deploying Machine Learning Models](./)
* Previous: [Serving the churn model with Flask](04-flask-deployment.md)
* Next: [Environment management: Docker](06-docker.md)
