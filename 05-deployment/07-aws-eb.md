## 5.7 Deployment to the cloud: AWS Elastic Beanstalk (optional)

<a href="https://www.youtube.com/watch?v=HGPJ4ekhcLg&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-07.jpg"></a>

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Links

* [Creating an account on AWS](https://mlbookcamp.com/article/aws)


## Notes
As we see how to deploy our apps in AWS Let's find it out how to deploy them in Heroku.
#### Heroku
Here we will learn how to deploy our apps in heroku instead of AWS.
- First of all create your web service with flask. (example file: [churn_prediction.py](https://github.com/amindadgar/customer-churn-app/blob/main/churn_serving.py)
- Then create a file named _requirements.txt_ and pass your dependencies there. Example:
 ```
 pickle
 numpy
 flask
 gunicorn
  ```
- Create another file named _Procfile_ and add the app you want to be able to run there. Example:
 ```
web: gunicorn churn_serving:app
  ```
  Note that the churn_serving name in the box above is the name of the main python file we're going to be running.
 - Create your heroku profile, Go to dashboard and the Deploy tab.
 - Follow the instruction to Deploy using Heroku Git.
 - Great, your app is now available from global universe.

I've put my heroku app files in this repository:
https://github.com/amindadgar/customer-churn-app 


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
* [Session 5: Deploying Machine Learning Models](./)
* Previous: [Environment management: Docker](06-docker.md)
* Next: [Summary](08-summary.md)
