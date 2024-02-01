# Resources for Kubernetes (k8s) for the project

Resources kubernetes to install in the cluster for the app of project to work.

## Ingress Controller Nginx

```bash
kubectl apply -f ingress_controller.yml
```

## Cert-Manager (Let's Encrypt)

```bash
helm repo add jetstack https://charts.jetstack.io --force-update
helm repo update
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.3/cert-manager.crds.yaml
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.13.3 \
  # --set installCRDs=true
```

## Issuer Let's Encrypt - Staging

```bash
kubectl apply -f issuer_letsencrypt_staging.yml
```

## Issuer Let's Encrypt - Production

```bash
kubectl apply -f issuer_letsencrypt_production.yml
```

> **NOTE** The issuer must be installed in the same namespace as the app.