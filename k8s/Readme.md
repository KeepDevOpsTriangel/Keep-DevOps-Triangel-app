# Resources for Kubernetes (k8s) for the project
# Necessary resources for our project to work in a k8s cluster

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

## Sealed Secrets

```bash
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm repo update
helm install sealed-secrets-controller sealed-secrets/sealed-secrets -n kube-system

# Create secret **token.yaml** with data token to be sealed

apiVersion: v1
kind: Secret
metadata:
  name: secret-token
  namespace: default
type: Opaque
stringData:
    TOKEN: xxxxxxxxxxx
    OPENAI_API_KEY: xxxxxxxxxxx

kubeseal --controller-name=sealed-secrets-controller --controller-namespace=kube-system --format yaml < token.yaml > secret-token.yaml

kubectl apply -f secret-token.yaml
```

