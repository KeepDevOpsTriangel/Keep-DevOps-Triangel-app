# EKS infrastructure by Terraform
This repository includes the required Terraform files to provision following components,
- Single node group EKS cluster 
- AWS Load Balancer Controller
- ArgoCD server exposed by AWS Application Load Balancer


# Usage
1. Open the terminal and run aws configure. Follow the prompts and input your credentials.
```
aws configure

    acces key: 
    Secret access key:
```

2. Initialize terraform dependencies by,
```
terraform init
```
3. Get the list of resources being created by,
```
terraform plan
```
5. Create the planned resources by,
```
terraform apply
```

despues de desplegar el cluster de eks, se tiene que descomentar el resource "kubernetes_manifest" "issuer_letsencrypt_prod" de  8-cert-manager.tf

## Outputs

- `argocd_ingress_service_name`: This is the URL through which ArgoCD can be accessed.


- `kubeconfig_command`: The command to update the kubeconfig file for the dev-cluster.

- `comaand pass` : kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d




