## 9. Serverless Deep Learning


Use the [workshop](workshop/) for most of the content.

The content in the module still works, but most of it is outdated
and doesn't work with newer version of Python.

Check 9.1 and 9.2 for introduction, but for the rest of the module, 
use the workshop materials. Also, unit 9.7 could still be relevant.

- 9.1 [Introduction to Serverless](01-intro.md) - Introduce deploying the clothing classifier as a web service with AWS Lambda and TensorFlow Lite.
- 9.2 [AWS Lambda](02-aws-lambda.md) - Create and test a first Lambda function in the AWS console and compare serverless billing with running a server.
- (Outdated) 9.3 [TensorFlow Lite](03-tensorflow-lite.md) - Convert the Keras model to TensorFlow Lite and run predictions with the interpreter and without TensorFlow.
- (Outdated) 9.4 [Preparing the code for Lambda](04-preparing-code.md) - Convert the notebook into a Python predict function and Lambda handler, then test them locally.
- (Outdated) 9.5 [Preparing a Docker image](05-docker-image.md) - Package the prediction script and TF Lite model into a Docker image, fix two errors, and test it locally.
- (Outdated) 9.6 [Creating the lambda function](06-creating-lambda.md) - Push the Docker image to Amazon ECR, create a Lambda container function, set its timeout and memory, and estimate cost.
- 9.7 [API Gateway: exposing the lambda function](07-api-gateway.md) - Expose the Lambda function as a POST /predict endpoint through API Gateway and test it with a deployed URL.
- 9.8 [Summary](08-summary.md) - Recap the serverless module on Lambda, Docker, TensorFlow Lite size savings and API Gateway.
- 9.9 [Explore more](09-explore-more.md) - Suggest other serverless options and show deploying the Lambda container with AWS SAM CLI.
- 9.10 [Python 3.12 vs TF Lite 2.17](10-updates.md) - Pin Python 3.10, numpy 1.23.1 and TF Lite 2.14 to serve TensorFlow 2.17 models on Lambda.



## Community notes

Did you take notes? You can share them here (or in each unit separately)

* [Alvaro Navas' Notes](https://github.com/ziritrion/ml-zoomcamp/blob/main/notes/09_serverless.md)
* [Notes from froukje](https://github.com/froukje/ml-zoomcamp/blob/main/week9/Lecture_9_serverless.ipynb)
* [Notes from Memoona Tahira](https://github.com/MemoonaTahira/MLZoomcamp2022/tree/main/Notes/Week_9-Serverless)
* [Notes from Oscar Garcia](https://github.com/ozkary/machine-learning-engineering/tree/main/09-serverless)
* [Notes from Peter Ernicke](https://knowmledge.com/category/courses/ml-zoomcamp/serverless-deployment/)
* [Notes from Maximilien Eyengue](https://github.com/maxim-eyengue/Python-Codes/blob/main/ML_Zoomcamp_2024/09_serverless/Summary_Session_09.md)
* Add your notes here
