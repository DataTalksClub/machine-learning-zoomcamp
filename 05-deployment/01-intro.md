
## 5.1 Intro / Session overview

<a href="https://www.youtube.com/watch?v=agIFak9A3m8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-01.jpg"></a>
 

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Notes


In this session, we talked about the earlier model we made in chapter 3 for churn prediction. <br>
This chapter contains the deployment of the model. If we want to use the model to predict new values without running the code, there's a way to do this. The way to use the model in different machines without running the code, is to deploy the model in a server (run the code and make the model). After deploying the code in a machine used as server we can make some endpoints (using api's) to connect from another machine to the server and predict values.

Model deployment is crucial when you need to use the model across different machines or applications without having to retrain or rerun the code. By deploying the model as a web service, external systems (like marketing services) can send requests to the server to get predictions, such as whether a customer is likely to churn. Based on the prediction, actions like sending promotional offers can be automated.

To deploy the model in a server there are some steps:
1. **Train and Save the Model**: After training the model, save it as a file, to use it for making predictions in future (session 02-pickle).
2. **Create API Endpoints**: Make the API endpoints in order to request predictions. It is possible to use the Flask framework to create web service API endpoints that other services can interact with (session 03-flask-intro and 04-flask-deployment).
3. **Some other server deployment options** (sessions 5 to 9):
   - **Pipenv**: Create isolated environments to manage the Python dependencies of the web service, ensuring they don’t interfere with other services on the machine.
   - **Docker**: Package the service in a Docker container, which includes both system and Python dependencies, making it easier to deploy consistently across different environments. 
4. **Deploy to the Cloud**: Finally, deploy the Docker container to a cloud service like AWS to make the model accessible globally, ensuring scalability and reliability.

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

* [Notes from Peter Ernicke](https://knowmledge.com/2023/10/09/ml-zoomcamp-2023-deploying-machine-learning-models-part-1/)

## Navigation

* [Machine Learning Zoomcamp course](../)
* [Session 5: Deploying Machine Learning Models](./)
* Next: [Saving and loading the model](02-pickle.md)
