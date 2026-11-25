#!/usr/bin/env bash
# Deploy the dropout API to a local Kubernetes cluster with kind, then test it.
# Needs: docker, kind, kubectl.  Run from the project root:  bash k8s/deploy-kind.sh
set -euo pipefail

CLUSTER=dropout
IMAGE=dropout-api:v1

docker build -t "$IMAGE" .

if ! kind get clusters | grep -qx "$CLUSTER"; then
  kind create cluster --name "$CLUSTER"
fi
kind load docker-image "$IMAGE" --name "$CLUSTER"

kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml
kubectl rollout status deployment/dropout-api --timeout=120s
kubectl get pods -l app=dropout-api

# Forward the service to localhost:9696 and send the example requests
kubectl port-forward service/dropout-api 9696:80 >/dev/null 2>&1 &
PF_PID=$!
trap 'kill $PF_PID' EXIT
sleep 3
python test_service.py http://localhost:9696

echo
echo "Done. To remove everything:  kind delete cluster --name $CLUSTER"
