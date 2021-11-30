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
```