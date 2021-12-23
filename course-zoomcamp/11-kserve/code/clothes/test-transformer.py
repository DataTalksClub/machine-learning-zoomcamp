#!/usr/bin/env python
# coding: utf-8

import requests


service_name = 'clothes'
host = f'{service_name}.default.example.com'

actual_domain = 'http://localhost:8080'
service_url = f'{actual_domain}/v1/models/{service_name}:predict'

headers = {'Host': host}


request = {
    "instances": [
        {'url': 'http://bit.ly/mlbookcamp-pants'},
        {'url': 'http://bit.ly/mlbookcamp-pants'}
    ]
}


response = requests.post(service_url, json=request, headers=headers)

print(response)
print(response.content)
print(response.json())
