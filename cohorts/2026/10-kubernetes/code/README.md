```
saved_model_cli

docker run -it --rm \
  -p 8500:8500 \
  -v $(pwd)/clothing-model:/models/clothing-model/1 \
  -e MODEL_NAME="clothing-model" \
  tensorflow/serving:2.7.0


docker build -t zoomcamp-10-model:xception-v4-001 \
  -f image-model.dockerfile .

docker run -it --rm \
  -p 8500:8500 \
  zoomcamp-10-model:xception-v4-001

docker build -t zoomcamp-10-gateway:002 \
  -f image-gateway.dockerfile .

docker run -it --rm \
  -p 9696:9696 \
  zoomcamp-10-gateway:001


docker-compose up

docker-compose up -d
docker-compose down

docker build -t ping:v001 .
docker run -it --rm -p 9696:9696 ping:v001


kind create cluster

kubectl get service
kubectl get pod
kubectl get deployment

kubectl apply -f deployment.yaml

kind load docker-image ping:v001
kubectl port-forward ping-deployment-7df687f8cd-tfkgd 9696:9696

kubectl apply -f service.yaml
kubectl port-forward service/ping 8080:80

kind load docker-image zoomcamp-10-model:xception-v4-001

kubectl port-forward tf-serving-clothing-model-85cd4b7fc9-rntfw 8500:8500

kubectl port-forward service/tf-serving-clothing-model 8500:8500

kind load docker-image zoomcamp-10-gateway:002

kubectl exec -it ping-deployment-577d56ccf5-p2bdq -- bash

apt update
apt install curl telnet 
telnet tf-serving-clothing-model.default.svc.cluster.local 8500

kubectl port-forward service/gateway 8080:80


ACCOUNT_ID=387546586013
REGION=eu-west-1
REGISTRY_NAME=mlzoomcamp-images
PREFIX=${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY_NAME}

GATEWAY_LOCAL=zoomcamp-10-gateway:002
GATEWAY_REMOTE=${PREFIX}:zoomcamp-10-gateway-002
docker tag ${GATEWAY_LOCAL} ${GATEWAY_REMOTE}

MODEL_LOCAL=zoomcamp-10-model:xception-v4-001
MODEL_REMOTE=${PREFIX}:zoomcamp-10-model-xception-v4-001
docker tag ${MODEL_LOCAL} ${MODEL_REMOTE}

docker push ${MODEL_REMOTE}
docker push ${GATEWAY_REMOTE}


eksctl create cluster -f eks-config.yaml
eksctl delete cluster --name mlzoomcamp-eks
```