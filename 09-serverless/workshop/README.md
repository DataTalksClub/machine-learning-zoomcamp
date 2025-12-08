# Machine Learning and Deep Learning Model Deployment with Serverless

* Video: https://www.youtube.com/watch?v=sHQaeVm5hT8

In this workshop we will revise [he Serverless module (Module 9)](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/master/09-serverless) of 
[Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp).

In the module, we

- Convert a model into TF-lite representation
- Deploy it with Lambda and Docker

This approach is no longer usable today:

- The latest versions of TF-lite are very difficult to compile for the target platform (Amazon Linux) (see the old approach [here](https://github.com/alexeygrigorev/tflite-aws-lambda))
- They are also becoming heavier

In this workshop, we want to revise this module and redo it from scratch:

- First, we want to talk about deploying usual ML models - i.e. models created with Scikit-Learn 
- Then we will look at deploying Deep Learning models

## Plan

The plan for the workshop:

- Creating a simple AWS Lambda function
- Deploying Scikit-Learn models with Docker
- Using ONNX for Keras and TF models
- ONNX for PyTorch models

## Prerequisites

- [AWS Account](https://mlbookcamp.com/article/aws)
- [AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Scikit-Learn Models

First, let's train a simple scikit-learn model that we will later deploy

We will take the [train.py](train/train.py) script (slightly adjusted) from the [uv+FastAPI workshop](../../05-deployment/workshop/).

```bash
cd train
uv sync
uv run python train.py
```

As the result, you will have [model.bin](train/model.bin) - this is what we're going to deploy in the first part of the workshop.


## AWS Lambda

First, let's look at the simplest AWS Lambda application.

We will send a request, and it will look at it, and respond with 
a prediction. 

Let's create a file `lambda_function.py`
(see [`lambda-sklearn/`](lambda-sklearn/)):

```python
def predict_single(customer):
    # we will put our model here
    return 0.56

def lambda_handler(event, context):    
    print("Parameters:", event)
    customer = event['customer']
    prob = predict_single(customer)
    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }
```

Let's "deploy" it: 

- Go to AWS -> Lambda
- Click "Create Function"
- Author from scratch
    - Name: "churn-prediction"
    - Runtime: Python 3.13
    - Default execution role: create a new one (selected by default)
    - Additional configuration - keep as is
- Put the code there

Now let's test it. Deploy it, click test, then create a new event with the
following data:

```json
{
  "customer": {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
  }
}
```

We see the predictions:

```json
{
  "churn_probability": 0.56,
  "churn": true
}
```

Invoking with CLI: 

```bash
aws lambda invoke \
  --function-name churn-prediction \
  --cli-binary-format raw-in-base64-out \
  --payload file://lambda-1-simple/customer.json \
  output.json
```

or with boto3 (`pip install boto3`):

```python
import boto3
import json

lambda_client = boto3.client('lambda')

customer = ...

response = lambda_client.invoke(
    FunctionName='churn-prediction',
    InvocationType='RequestResponse',
    Payload=json.dumps(customer)
)

result = json.loads(response['Payload'].read())
print(json.dumps(result, indent=2))
```

You can also expose it as a web service (see [unit 9.7 about API Gateway](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/09-serverless/07-api-gateway.md)).


## AWS Lambda with Docker: Running Locally

How do we add the actual model?

That's how we load it:

```python
import pickle

with open('model.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)
```

But for that we need to package the dependencies
along with our code in a single ZIP archive.

The problem: Scikit-Learn with all the dependencies takes 
more than 250 mb. And this is a limit for the ZIP
archive.

If we add everything in Docker, we won't have
this problem. So let's do it

Copy our model:

```bash
cp ../train/model.bin .
```

Define the Dockerfile (based on [this](https://github.com/alexeygrigorev/workshops/blob/main/mlzoomcamp-fastapi-uv/Dockerfile)):

```dockerfile
FROM public.ecr.aws/lambda/python:3.13
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY pyproject.toml uv.lock ./
RUN uv pip install --system -r <(uv export --format requirements-txt)

COPY lambda_function.py model.bin ./

CMD ["lambda_function.lambda_handler"]
```

Build it:

```bash
docker build -t churn-prediction-lambda .
```

Run it:

```bash
docker run -it --rm -p 8080:8080  churn-prediction-lambda
```

Test it:

```python
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

result = requests.post(url, json=customer).json()
print(result)
```

Or run

```bash
python test.py
```

Note that since we can run it locally,
we can test a lot of things without deploying

## AWS Lambda: Deployment

It's time to deploy our Lambda to AWS. 

Since we use Docker, we'll need to create a registry

You can do it through the web interface, but we'll save time and do it with AWS CLI:

```bash
aws ecr create-repository \
  --repository-name "churn-prediction-lambda" \
  --region "eu-west-1"
```

You will get a response like that:

```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:eu-west-1:387546586013:repository/churn-prediction-lambda",
        "registryId": "387546586013",
        "repositoryName": "churn-prediction-lambda",
        "repositoryUri": "387546586013.dkr.ecr.eu-west-1.amazonaws.com/churn-prediction-lambda",
        "createdAt": "2025-08-15T11:21:46.389000+02:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```
Note `repositoryUri`. It will look like this: `"387546586013.dkr.ecr.eu-west-1.amazonaws.com/churn-prediction-lambda"`

Here we have two parts:

- First, ECR URL: `387546586013.dkr.ecr.eu-west-1.amazonaws.com`
  - Your account
  - The region
- The name of the repository

Let's put the ECR URL into a variable:

```bash
ECR_URL="387546586013.dkr.ecr.eu-west-1.amazonaws.com"
```

Now login to that repo with Docker:

```bash
aws ecr get-login-password \
  --region "eu-west-1" \
| docker login \
  --username AWS \
  --password-stdin ${ECR_URL}
```

Now we tag our docker image with a special tag,
and then push it to ECR:

```bash
REMOTE_IMAGE_TAG="${ECR_URL}/churn-prediction-lambda:v1"

docker build -t churn-prediction-lambda .
docker tag churn-prediction-lambda ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}
```

Now go to Lambda:

* Create function
* Select "Container image"
* Name: "churn-prediction-docker"
* Select your container image
* Create function
* You may need to increase timeout to 30 seconds(Configuration -> General Configuration -> Edit)
* Testing is the same as before
* The first execution may take longer (it pull docker image, etc), but subsequent executions are faster

```json
{
  "customer": {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
  }
}
```


If you have problems with ECR permissions,
create a policy with name "Lambda-ECR-Read":

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:GetAuthorizationToken"
      ],
      "Resource": "arn:aws:ecr:eu-west-1:387546586013:repository/*"
    }
  ]
}
```

And attach this policy to the lambda's role.

Updating the lambda with AWS CLI:

```bash
REMOTE_IMAGE_TAG="${ECR_URL}/churn-prediction-lambda:v2"

docker build -t churn-prediction-lambda .
docker tag churn-prediction-lambda ${REMOTE_IMAGE_TAG}
docker push ${REMOTE_IMAGE_TAG}


aws lambda update-function-code \
  --function-name churn-prediction-docker \
  --image-uri ${REMOTE_IMAGE_TAG} \
  --region eu-west-1
```

You can check [`deploy.sh`](lambda-sklearn/deploy.sh) for a little more advanced version
of the deployment process.

You can ask ChatGPT to explain you this script.

Invoking the function is the same as before. See [`invoke.py`](lambda-sklearn/invoke.py).

## AWS Lambda: TensorFlow Models

Previously we used TF-lite for AWS Lambda. 

In this workshop, we'll use an alternative - ONNX (Open Neural Network Exchange).

We need will use the same Keras model as before.
It was retrained for the newest TF version, you
can see [here](https://colab.research.google.com/drive/1GTkGkq1QKOtAL0wiMjYr-LOCpVgsAwyk?usp=sharing) the training process.

Let's download the model:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing-model-new.keras
```

Converting to ONNX happens in 2 steps:

- First, convert it into the saved_model format of TensorFlow
- Second, convert the saved_model format into ONNX.

For the second step, we will need to install tf2onnx:

```bash
# normally you install it with pip like that:
# pip install tf2onnx
# but the last release (Jan 2025) doesn't contain numpy 2 update
# so install it from github directly:

pip install git+https://github.com/onnx/tensorflow-onnx.git
```

First step:

```python
from tensorflow import keras

model = keras.models.load_model('clothing-model-new.keras')
model.export("clothing-model-new_savedmodel")
```

Second step:

```bash
python -m tf2onnx.convert \
    --saved-model clothing-model-new_savedmodel \
    --opset 13 \
    --output clothing-model-new.onnx
```

To avoid version conflicts between TensorFlow and ONNX, let's do it in Docker:

```bash
cd convert 

# you can update it to the latest commit
COMMIT_ID=c34ac1d751427cf5d98023a21cce4c82b0cf96a1
TAG=${COMMIT_ID:0:7}

docker build \
  --build-arg COMMIT_ID=$COMMIT_ID \
  -t tensorflow-onnx-runtime:$TAG .

# it may take some time to build the image
# if you don't want to build it yourself, use my build:
# agrigorev/tensorflow-onnx-runtime

mkdir models

cp ../clothing-model-new.keras models/clothing-model-new.keras
cp ../convert-saved-model.py models/convert-saved-model.py

docker run -it --rm \
  -v $(pwd)/models:/models \
  tensorflow-onnx-runtime:$TAG


# on gitbash, you may need to do /$(pwd)/models
python convert-saved-model.py

python -m tf2onnx.convert \
    --saved-model clothing-model-new_savedmodel \
    --opset 13 \
    --output clothing-model-new.onnx

exit
```

You can download the results here:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing-model-new.onnx
```

Now our models are saved in the ONNX format. Like with TF-lite,
we only need ONNX-Runtime to run it:

```bash
pip install onnxruntime
```

Like in the module, we can't use TF for our preprocessing. That's 
why we will rely on `keras-image-helper` to do that:

```bash
pip install keras-image-helper
```

This is how you use ONNX-Runtime to make predictions:

```python
import onnxruntime as ort

onnx_model_path = "clothing-model-new.onnx"
session = ort.InferenceSession(onnx_model_path, providers=["CPUExecutionProvider"])

inputs = session.get_inputs()
outputs = session.get_outputs()

input_name = inputs[0].name
output_name = outputs[0].name
```

Get the image:

```python
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(299, 299))

url = 'http://bit.ly/mlbookcamp-pants'
X = preprocessor.from_url(url)
```

Make predictions:

```python
result = session.run([output_name], {input_name: X})
predictions = result[0][0].tolist()

classes = [
    'dress',
    'hat',
    'longsleeve',
    'outwear',
    'pants',
    'shirt',
    'shoes',
    'shorts',
    'skirt',
    't-shirt'
]

dict(zip(classes, predictions))
```

Let's package this into a lambda function:

```python
import onnxruntime as ort
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor("xception", target_size=(299, 299))

session = ort.InferenceSession(
    "clothing-model-new.onnx", providers=["CPUExecutionProvider"]
)
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

classes = [
    "dress",
    "hat",
    "longsleeve",
    "outwear",
    "pants",
    "shirt",
    "shoes",
    "shorts",
    "skirt",
    "t-shirt",
]


def predict(url):
    X = preprocessor.from_url(url)
    result = session.run([output_name], {input_name: X})
    float_predictions = result[0][0].tolist()
    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
```

Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/python:3.13

RUN pip install onnxruntime keras-image-helper

COPY clothing-model-new.onnx clothing-model-new.onnx
COPY lambda_function.py ./

CMD ["lambda_function.lambda_handler"]
```

Build and run:

```bash
docker build -t clothing-lambda-keras .
docker run -it --rm -p 8080:8080 clothing-lambda-keras
```

Testing it:

```python
import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

request = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

result = requests.post(url, json=request).json()
print(result)
```

## AWS Lambda: PyTorch Models

With PyTorch, we can do the same:

- Convert a model to ONNX
- Serve it with the same code as before

Here's a model [we trained with PyTorch](https://colab.research.google.com/drive/1_kvvbi_msBuTFkkdLxMEpB3mj-Jhh-Bc?usp=sharing):

In PyTorch, when we train a model, we can save it directly to ONNX:

```python
torch.onnx.export(
    model,
    input,
    onnx_path,
    ...
)
```

So we can just download our model:

```bash
wget https://github.com/DataTalksClub/machine-learning-zoomcamp/releases/download/dl-models/clothing_classifier_mobilenet_v2_latest.onnx
```

The rest of the code stays the same - we already know how to load and serve ONNX.

We need to adjust our preprocessor - PyTorch uses a different
format (not `BCHW`, but `BHWC`, where `B` is batch, `C` is channel, `W` is width and `H` is height).

You can see [`lambda_function.py`](lambda-onnx/lambda_function.py) or [`test.ipynb`](lambda-onnx/test.ipynb) for details.

Let's build and run it:

```bash
docker build -t clothing-lambda-onnx .
docker run -it --rm -p 8080:8080 clothing-lambda-onnx
```

Test:

```bash
python test.py
```

That's all!

## Summary

We covered:

1. **Scikit-Learn Model Deployment**
   - Training a simple ML model for churn prediction
   - Basic AWS Lambda function creation and testing
   - Docker containerization to overcome size limitations
   - ECR deployment and AWS Lambda container image deployment

2. **Deep Learning Model Deployment with ONNX**
   - Converting TensorFlow/Keras models to ONNX format
   - Converting PyTorch models to ONNX format
   - Using ONNX Runtime for efficient inference
   - Docker-based deployment for deep learning models

**Next Steps:**

- Explore API Gateway integration for web service exposure
- Implement monitoring and logging with CloudWatch
- Consider using AWS Step Functions for complex ML workflows
- Explore other serverless services like AWS Batch for training

