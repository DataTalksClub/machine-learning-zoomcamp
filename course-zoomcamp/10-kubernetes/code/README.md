```
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

kubectl port-forward tf-serving-clothing-model-85cd4b7fc9-rntfw 8500:8
500
kubectl port-forward service/tf-serving-clothing-model 8500:8500

kind load docker-image zoomcamp-10-gateway:002

kubectl exec -it ping-deployment-577d56ccf5-p2bdq -- bash
```