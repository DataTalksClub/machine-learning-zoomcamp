---
video_url: https://www.youtube.com/watch?v=BMXh8JGROHM&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR
code:
  - label: Pipfile
    path: code/Pipfile
---
# Python virtual environment: Pipenv

In this unit we put the project's dependencies into an isolated virtual
environment with Pipenv, so our service always runs with the library versions
we tested it with.

## The problem: conflicting library versions

When we install Python packages with `pip install`, they all go to one shared
place - the system-wide Python installation. That works until two projects
need different versions of the same library. An old project may need
scikit-learn 0.24, while a new one wants the latest 1.0 - upgrade for one, and
the other breaks.

The fix is a virtual environment: a private set of packages for one project.
Each project gets its own versions, and they don't interfere with each other
or with the system Python.

There are many tools for this - `venv`, `conda`, `poetry`. In this course we
use Pipenv, because besides creating the environment it also records the exact
package versions, which is what we need to reproduce the environment on a
server later.

## Installing libraries with Pipenv

Install Pipenv itself once, system-wide:

```bash
pip install pipenv
```

Then, inside the project directory, add the project dependencies - for our
churn service that is numpy, scikit-learn, flask and gunicorn:

```bash
pipenv install numpy scikit-learn flask gunicorn
```

This command creates a virtual environment and installs the packages into it.
It also creates two files in the project directory:

- Pipfile - the list of packages the project depends on, with the versions we
  asked for. For our project it looks like this:

  ```toml
  [[source]]
  url = "https://pypi.org/simple"
  verify_ssl = true
  name = "pypi"

  [packages]
  numpy = "*"
  scikit-learn = "==0.24.2"
  flask = "*"
  gunicorn = "*"

  [dev-packages]

  [requires]
  python_version = "3.8"
  ```

- Pipfile.lock - the exact version of every installed package, including the
  dependencies of the dependencies, together with hashes. With the lock file,
  the same environment can be reproduced bit by bit on any other machine.

It is the lock file that makes deployments predictable: "works on my machine"
stops being a mystery, because the server installs precisely what we tested.

## Running things with Pipenv

On another machine - or after cloning the project - one command recreates the
environment from the two files:

```bash
pipenv install
```

To use the environment, open a shell inside it:

```bash
pipenv shell
```

Inside this shell, `python` and every command use the virtual environment's
packages, so we can start the service as usual:

```bash
gunicorn --bind localhost:9696 predict:app
```

Typing `exit` leaves the environment. If we prefer a single command without
activating the shell first, we can run the command through pipenv directly:

```bash
pipenv run gunicorn --bind localhost:9696 predict:app
```

At this point the service runs with pinned, reproducible dependencies. What
is still tied to our machine is Python itself and everything outside Python
packages. In the [next unit](06-docker.md) we put the whole environment - the
Python version included - into a Docker container.

## Materials

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
