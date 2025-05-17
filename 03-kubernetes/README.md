# Kubernetes

Для начала необходимо установить ingress контролллер (nginx) в кластер k8s, я делал локально с помощью minikube.
После этого можно применять манифесты в следующем порядке:
```bash
cd manifests
kubectl apply -f namespace.yaml
kubectl apply -f imagePullSecret.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f deployment.yaml
```
