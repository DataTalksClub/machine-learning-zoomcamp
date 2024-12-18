
## 9.2 AWS Lambda

<a href="https://www.youtube.com/watch?v=_UX8-2WhHZo&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR"><img src="images/thumbnail-9-02.jpg"></a>

 AWS Lambda is a **serverless computing service** that lets you execute code without worrying about managing servers. Here's an overview of how it works and its benefits:  

### **Setting Up a Lambda Function 🛠️**
1. **Accessing Lambda:**
   - Go to the AWS Management Console and search for the `Lambda` service.

2. **Creating a Function:**
   - Choose the `Author from scratch` option.
   - Name your function (e.g., `mlzoomcamp-test`).
   - Select the runtime environment (e.g., `Python 3.9`) and architecture (`x86_64`).

3. **Understanding Function Parameters:**
   - **`event`:** Contains the input data passed to the function (e.g., a JSON payload).
   - **`context`:** Provides details about the invocation, configuration, and execution environment.

4. **Updating the Default Function:**
   - Edit `lambda_function.py` with custom logic. Example:  
     ```python
     def lambda_handler(event, context):
         print("Parameters:", event) # Print input parameters
         url = event["url"]  # Extract URL from input
         return {"prediction": "clothes"}  # Sample response
     ```

### **Testing and Deployment 🚀**
1. **Create a Test Event:**
   - Define a mock input to simulate real-world data.  

2. **Deploy Changes:**
   - Save and deploy the function to apply updates.  

3. **Test Your Function:**
   - Run the function with the test event to ensure it works as expected.

### **Advantages of AWS Lambda ✅**
- **Serverless Architecture 🖥️:** No need to provision or manage servers.  
- **Cost-Effective 💰:** Pay only for requests and compute time—idle time is free!  
- **Automatic Scaling 📈:** Adjusts automatically based on request volume.  
- **Ease of Use 🎯:** Focus on coding; AWS handles infrastructure.  

### **Dynamic Link Management Use Case 🌐**
 `AWS lambda` was used to automatically redirect users to updated invite links for joining the DataTalks.Club community. This is to avoid expired links on the user side, by using a Lambda function that reads from a config file where invitation links can be update.  

### Free Tier Usage
Note that `AWS Lambda` offers a free tier that includes a certain number of free requests (1 million requests per month), and free compute time (400,000 GB-seconds per month).



## Notes

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
* [Session 9: Serverless Deep Learning](./)
* Previous: [Introduction to Serverless](01-intro.md)
* Next: [TensorFlow Lite](03-tensorflow-lite.md)
