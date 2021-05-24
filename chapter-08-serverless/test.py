import requests

data = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

url = "http://localhost:8080/2015-03-31/functions/function/invocations"
# url = "https://0a1v3fyo2m.execute-api.eu-west-1.amazonaws.com/test/predict"

results = requests.post(url, json=data).json()

print(results)