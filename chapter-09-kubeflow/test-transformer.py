import requests

data = {
    "instances": [
        {"url": "http://bit.ly/mlbookcamp-pants"},
    ]
}

# url = 'http://localhost:8080/v1/models/clothing-model:predict'

url = 'https://clothing-model.default.kubeflow.mlbookcamp.com/v1/models/clothing-model:predict'

result = requests.post(url, json=data).json()

print(result)
