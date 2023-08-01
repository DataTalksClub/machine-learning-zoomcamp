
```bash
kubectl port-forward -n istio-system service/istio-ingressgateway 8080:80


SERVICE_NAME="sklearn-iris"
HOST="${SERVICE_NAME}.default.example.com"
ACTUAL_HOST="http://localhost:8080"
URL="${ACTUAL_HOST}/v1/models/${SERVICE_NAME}:predict"

curl -H "Host: ${HOST}" \
    ${URL} \
   -d @iris-request.json


docker build -t kserve-sklearnserver:predict_proba-3.8-1.0 -f  sklearn.Dockerfile .

docker run -it --rm \
    -v "$(pwd)/model.joblib:/mnt/models/model.joblib" \
    -p 8081:8080 \
    kserve-sklearnserver:predict_proba-3.8-1.0 \
    --model_dir=/mnt/models \
    --model_name=churn
```