
```bash
# you can update it to the latest commit
COMMIT_ID=c34ac1d751427cf5d98023a21cce4c82b0cf96a1
TAG=${COMMIT_ID:0:7}

docker build \
  --build-arg COMMIT_ID=$COMMIT_ID \
  -t tensorflow-onnx-runtime:$TAG .


docker login

docker tag tensorflow-onnx-runtime:$TAG agrigorev/tensorflow-onnx-runtime:$TAG
docker push agrigorev/tensorflow-onnx-runtime:$TAG

docker tag tensorflow-onnx-runtime:$TAG agrigorev/tensorflow-onnx-runtime:latest
docker push agrigorev/tensorflow-onnx-runtime:latest
```