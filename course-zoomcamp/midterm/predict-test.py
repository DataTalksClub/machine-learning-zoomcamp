#!/usr/bin/env python
# coding: utf-8

import requests


url = 'http://localhost:9696/predict'

passanger = {
    "passengerid": "8", 
    "pclass": 3,
    "name": "Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)",
    "sex": "female",
    "age": "27.0",
    "sibsp": "0",
    "parch": "2",
    "ticket": "347742", 
    "fare": "11.1333", 
    "embarked": "S", 
    "cabin": "NaN"
}

response = requests.post(url, json=passanger).json()
print(response)
