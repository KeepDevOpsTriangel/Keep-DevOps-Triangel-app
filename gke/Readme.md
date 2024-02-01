# Infrastructure as Code with Terraform

Deploying a Kubernetes cluster on Google Cloud Platform (GCP) using Terraform, and deploying an application on the cluster using ArgoCD and Helm.

## Resources created

- Kubernetes cluster on GCP (GKE)
- ArgoCD application on the cluster in the namespace argocd using Helm
- Ingess controller on the cluster for ArgoCD

## Prerequisites

- Terraform 1.6.6 or later
- Kubectl
- Google Cloud SDK
- Gcloud command line tool
- Account on Google Cloud Platform

## Deployment of Kubernetes cluster on GCP using Terraform

### Create a service account on GCP

Create a service account on GCP and download the credentials file in JSON format.

### Create a file terraform.tfvars

Create a file terraform.tfvars and add the following content:

```bash
project_id = "project_id"
credentials_file = "credentials_file.json"
resource_name = "resource_name"
region = "region"
zone = "zone"
```

### Initialize Terraform

```bash
terraform init
```

### Create a plan

```bash
terraform plan
```

### Apply the plan

```bash
terraform apply
```
>NOTE: At the end of the deployment of resources, show the password for user **admin** of ArgoCD in screen.

### Destroy the infrastructure

```bash
terraform destroy
```

## Sources

- [Terraform](https://www.terraform.io/)
- [Google Cloud Platform](https://cloud.google.com/)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
- [ArgoCD](https://argoproj.github.io/argo-cd/)
- [Helm](https://helm.sh/)
- [Kubectl](https://kubernetes.io/docs/reference/kubectl/overview/)
- [Google Cloud SDK](https://cloud.google.com/sdk)
- [Resource: helm_release](https://registry.terraform.io/providers/hashicorp/helm/latest/docs/resources/release)
- [kubectl](https://registry.terraform.io/providers/gavinbunney/kubectl/latest)
- [terraform-iaac/nginx-controller/helm](https://registry.terraform.io/modules/terraform-iaac/nginx-controller/helm/2.3.0?utm_content=documentLink&utm_medium=Visual+Studio+Code&utm_source=terraform-ls)
