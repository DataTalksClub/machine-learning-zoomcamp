import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

request = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

result = requests.post(url, json=request).json()
print(result)