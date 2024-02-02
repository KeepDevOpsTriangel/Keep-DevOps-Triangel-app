# Helm Charts for Triangle App

This directory contains the Helm charts for Triangle App [Triangle App](/app/Readme.md).

## Prerequisites

- Helm 3.0 or later
- Kubectl
- Cluster with Kubernetes 1.16 or later

## Installing the Chart

To install the chart with the release name `triangle-app`:

```bash
helm install triangle-app ./triangle-app
```

## Uninstalling the Chart

To uninstall the `triangle-app` deployment:

```bash
helm uninstall triangle-app
```

> ## NOTE:
> The helm chart needs a sealed secret to be created before deploying the chart. The sealed secret can be created using the following command:
> ```bash
> kubeseal --controller-name=sealed-secrets-controller --controller-namespace=kube-system --format yaml < token.yaml > sealed-secret.yaml
> **token.yaml** is the file containing the secret to be sealed - not included in the repository.
> ```