# Deployment of ArgoCD on Kubernetes

## Prerequisites

- Helm 3.0 or later
- Kubectl
- Cluster with Kubernetes 1.16 or later

## Deployment ArgoCD

```bash
helm upgrade --install --wait --timeout 15m --atomic --namespace argocd --create-namespace \
    --repo https://argoproj.github.io/argo-helm argocd argo-cd --values values.yaml
```
> This command will install a ArgoCD project in the namespace argocd and will use the values.yaml file to configure the project.

## Accessing ArgoCD

For obtain the password of the ArgoCD UI, execute the following command:

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

> ### Login with the user **admin** and the password obtained.
>----
