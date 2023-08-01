#!/usr/bin/env python
# coding: utf-8

import requests


service_name = 'clothes'
actual_domain = 'https://clothes.default.kubeflow.mlbookcamp.com'
service_url = f'{actual_domain}/v1/models/{service_name}:predict'

request = {
    "instances": [
        {'url': 'http://bit.ly/mlbookcamp-pants'},
        {'url': 'http://bit.ly/mlbookcamp-pants'}
    ]
}


response = requests.post(service_url, json=request)

print(response)
print(response.content)
print(response.json())
