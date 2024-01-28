# Deployment of ArgoCD on Kubernetes

## Prerequisites

- Helm 3.0 or later
- Kubectl
- Cluster with Kubernetes 1.16 or later

## Deployment ArgoCD on Kubernetes cluster local (minikube)

```bash
helm upgrade --install --wait --timeout 15m --atomic --namespace argocd --create-namespace \
    --repo https://argoproj.github.io/argo-helm argocd argo-cd --values values.yaml
```
> This command will install a ArgoCD project in the namespace argocd and will use the values.yaml file to configure the project.

## Deployment ArgoCD on Kubernetes cluster GKE

### Create a cluster GKE

Create a cluster GKE with the following command:

```bash
gcloud container clusters create argocd-cluster --zone europe-west1-b --num-nodes 1 --machine-type n1-standard-2
```

### Deploy ArgoCD on GKE

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Accessing ArgoCD

For obtain the password of the ArgoCD UI, execute the following command (user: admin):

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Check the ArgoCD project is running:
```bash	
kubectl get pods -n argocd
```

Access to the ArgoCD UI:
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open the browser and access to the following URL:
```bash
http://localhost:8080/argocd
```


## Deploying an application

The application's manifests for deployment in ArgoCD are stored in the `argocd` folder.

    The manifiest **app_cluster_default.yaml** is the definition of the application in ArgoCD for cluster default in local environment.

Login in ArgoCD with the user admin and the password obtained in the previous step, and create a new application with the manifest **app_cluster_default.yaml**.


