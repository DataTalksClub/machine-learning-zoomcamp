# Projects

See more information about projects and evaluation criteria [here](../../projects/)


## Getting a repository

To make it easier to review your project (and make it more useful
for you), we ask you to use this script for generating a GitHub 
repository 

```python
import requests

url = 'https://3was74r7p9.execute-api.eu-west-1.amazonaws.com/create_repository'

request = {
    'email': 'YOUR_EMAIL',
    'github': 'YOUR_GITHUB_HANDLE'
}

assert request['email'] != 'YOUR_EMAIL', "don't forget to put your email"
assert request['github'] != 'YOUR_GITHUB_HANDLE', "don't forget to put your github profile"

response = requests.post(url, json=request)
print(response.json())
```

The result will look like that:

```python
TODO
```

You can now clone this repository and start working on your project 


## Midterm Project

* Project due date: 7 November 2022
* Submit your project here: https://forms.gle/Hnk267ue7LPyR5bs5
* Evaluation due date: 14 November 2022
* Evaluation assignments: TBA
* Submit your evaluation here: TBA

## Capstone 1 

TBA

## Capstone 2 

TBA