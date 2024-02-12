# Deployment of ArgoCD on Kubernetes

## Prerequisites

- Helm 3.0 or later
- Kubectl
- Cluster with Kubernetes 1.16 or later

## Deployment ArgoCD on Kubernetes cluster local (minikube) using Helm

```bash
helm upgrade --install --wait --timeout 15m --atomic --namespace argocd --create-namespace \
    --repo https://argoproj.github.io/argo-helm argocd argo-cd --values values.yaml
```
> This command will install a ArgoCD project in the namespace argocd and will use the values.yaml file to configure the project.

## Deployment ArgoCD on cluster GKE

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```
> This command will install a ArgoCD project in the namespace argocd.

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

## Deploying an application using ArgoCD

Create a new application using the ArgoCD UI and use the manifest file located in the folder:
```bash
triangle-app.yaml
```

## Config Authentication with GitHub OAuth in ArgoCD

Edit the file argocd-cm.yaml and add the following configuration:

```bash
kubectl edit configmap argocd-cm -n argocd

data:
    url: https://argocdtriangleapp.rafaeltorices.com/argocd
    dex.config: |
    connectors:
      - type: github
        id: github
        name: GitHub
        config:
          clientID: xxxxxxxx
          clientSecret: xxxxxxxx
          redirectURI: https://argocdtriangleapp.rafaeltorices.com/argocd/api/dex/callback
          orgs:
          - name: KeepDevOpsTriangel

```

