
## Preparing

Get the model file:

```
wget https://github.com/alexeygrigorev/mlbookcamp-code/releases/download/chapter7-model/xception_v4_large_08_0.894.h5
```

Covert it:

```
python convert.py
```


Build the image:
```
docker build -t tf-lite-lambda .
```

## Running locally

To run locally

```
docker run --rm -p 8080:8080 tf-lite-lambda
```

Test it

```
python test.py
```


## Publishing

Create an ECR repo:

```
aws ecr create-repository --repository-name lambda-images
```

Login to Docker:

```
$(aws ecr get-login --no-include-email)
```


Publish the image:

```
REGION=eu-west-1
ACCOUNT=XXXXXXXXXXXX
REMOTE_NAME=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/lambda-images:tf-lite-lambda 
docker tag tf-lite-lambda ${REMOTE_NAME}
docker push ${REMOTE_NAME}
```

## Create a lambda function

* Go to Lambda, create a new function, select "container image"
* Put the image we just created there
* Go to basic settings and adjust timeout (30 sec) and memory (1GB)
* Test it with the following payload:

```json
{
    "url": "http://bit.ly/mlbookcamp-pants"
}
```

## Deploying

To deploy it with AWS Lambda and API Gateway, follow this tutorial: https://github.com/alexeygrigorev/aws-lambda-docker/blob/main/guide.md
