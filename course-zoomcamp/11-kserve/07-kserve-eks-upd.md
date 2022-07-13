## Deploying with KServe and EKS - Update (13 July, 2022)

(These instructions assume that the user does not own a custom domain.)  

- Download v1.21 of AWS' kubectl tool via  
 `https://s3.us-west-2.amazonaws.com/amazon-eks/1.21.2/2021-07-05/bin/linux/amd64/kubectl`
 
- Create a cluster (via `eksctl create cluster -f cluster.yaml`) using the following yaml file; note that we specify version 1.21 of k8s
 
 ```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: mlzoomcamp-eks
  region: us-east-2
  version: "1.21"

nodeGroups:
  - name: ng
    desiredCapacity: 2
    instanceType: m5.xlarge
```

- After downloading kserve==0.8 (via `wget https://raw.githubusercontent.com/kserve/kserve/release-0.8/hack/quick_install.sh`), set the version of Istio to 1.6.2 in line 33  
- Then run `bash quick_install.sh`

- Get the external IP from the ELB via  
`kubectl get services -n istio-system`

- Configure the secret key  
`kubectl apply -f kserve-s3-secret.yaml`  

- Create the Inference service  
`kubectl apply -f clothes-service.yaml`

- Create the file `test_transformer.py` with the following contents. Replace `actual_domain` with the external IP obtained from the ELB

```python
import requests


service_name = 'clothes'
host = f'{service_name}.default.example.com'

actual_domain = 'http://{something here}.us-east-2.elb.amazonaws.com'
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
```

- Run `python test-transformer3.py` 

- Delete cluster via `eksctl delete cluster --name mlzoomcamp-eks`
