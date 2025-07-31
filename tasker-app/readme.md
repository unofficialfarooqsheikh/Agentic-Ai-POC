Commands used to Deploy it to kubernetes

docker build -t iamgename:version .
## Deploy the app to kubernetes
kubectl apply -f flask-deployment.yaml
kubectl apply -f flask-service.yaml
## getting items
kubectl get pods
kubectl get svc
## Deleting items
kubectl delete service service_name
kubectl delete deployment deployment_name
kubectl delete pod -l app=flaskapp
## To Open Bash
kubectl exec -it taskerapp-796bbf95b5-mb7qt --bash
