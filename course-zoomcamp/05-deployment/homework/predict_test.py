import requests


url = 'http://0.0.0.0:9696/predict'

customer = customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 10}
result = requests.post(url, json=customer).json()
print(result)