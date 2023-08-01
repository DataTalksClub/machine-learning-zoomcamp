
## 5.3 Web services: introduction to Flask

<a href="https://www.youtube.com/watch?v=W7ubna1Rfv8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-5-03.jpg"></a>
 

[Slides](https://www.slideshare.net/AlexeyGrigorev/ml-zoomcamp-5-model-deployment)


## Links

* [0.0.0.0 vs localhost](https://stackoverflow.com/a/20778887/861423)

## Notes
In this session we talked about what is a web service and how to create a simple web service.
- What is actually a web service
  - A web service is a method used to communicate between electronic devices.
  - There are some methods in web services we can use it to satisfy our problems. Here below we would list some.
    - **GET:**  GET is a method used to retrieve files, For example when we are searching for a cat image in google we are actually requesting cat images with GET method.
    - **POST:** POST is the second common method used in web services. For example in a sign up process, when we are submiting our name, username, passwords, etc we are posting our data to a server that is using the web service. (Note that there is no specification where the data goes)
    -  **PUT:** PUT is same as POST but we are specifying where the data is going to.
    -  **DELETE:** DELETE is a method that is used to request to delete some data from the server.
    -  For more information just google the HTTP methods, You'll find useful information about this.
- To create a simple web service, there are plenty libraries available in every language. Here we would like to introduce Flask library in python.
  - If you haven't installed the library just try installing it with the code ```pip install Flask```
  - To create a simple web service just run the code below:
  - ```
    from flask import Flask
    app = Flask('churn-app') # give an identity to your web service
    @app.route('/ping',methods=[GET])
    def ping():
        return 'PONG'
    
    if __name__=='__main__':
       app.run('debug=True, host='0.0.0.0', port=9696) # run the code in local machine with the debugging mode true and port 9696
    ```
   - With the code above we made a simple web server and created a route named ping that would send pong string.
   - To test it just open your browser and search ```localhost:9696/ping```, You'll see that the 'PONG' string is received. Congrats You've made a simple web server 🥳.
- To use our web server to predict new values we must modify it. See how in the next session. 

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
* Previous: [Saving and loading the model](02-pickle.md)
* Next: [Serving the churn model with Flask](04-flask-deployment.md)
