# Kubernetes


## Manifests
Для начала необходимо установить ingress контролллер (nginx) в кластер k8s, я делал локально с помощью minikube.
```bash
minikube addons enable ingress
```
После этого можно применять манифесты в следующем порядке:
```bash
cd manifests
kubectl apply -f namespace.yaml
kubectl apply -f imagePullSecret.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f deployment.yaml
```

## Helm

Для проверки правильности написания Helm чарта я использовал следующую команду
```bash
helm template intern . -f values.yaml -n intern > manifest.yaml
```
