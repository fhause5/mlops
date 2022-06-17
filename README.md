# mlops
### Airflow

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-yaml

```commandline
C:\Users\<USER>\docker\airflow\
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.2/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up
localhost:8080, login with user “airflow” and password “airflow”
```

* PUT DAGS into: C:\Users\<USER>\docker\airflow\dags


### kubeflow

https://www.kubeflow.org/docs/distributions/azure/deploy/install-kubeflow/

### kubeflow on minikube

```commandline
minikube start --kubernetes-version=v1.18.10 --memory 8096 --cpus 4 --disk-size 60g --vm-driver virtualbox
minikube start -p minikube2 --kubernetes-version=v1.18.10
curl -O https://raw.githubusercontent.com/kubeflow/kubeflow/v0.2-branch/bootstrap/bootstrapper.yaml
kubectl create -f bootstrapper.yaml
```


### Data


* https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"