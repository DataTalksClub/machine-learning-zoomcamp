import requests 

service_name = 'sklearn-iris'
host = f'{service_name}.default.example.com'

actual_domain = 'http://localhost:8080' 
url = f'{actual_domain}/v1/models/{service_name}:predict'

headers = {
    'Host': host
}

request = {
    "instances": [
        [6.8,  2.8,  4.8,  1.4],
        [6.0,  3.4,  4.5,  1.6]
    ]
}

response = requests.post(url, json=request, headers=headers)
print(response.json())