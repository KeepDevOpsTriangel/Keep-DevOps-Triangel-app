######################################################################
## VPC

# Output the VPC ID
output "vpc_id" {
  value = module.vpc.vpc_id
}

######################################################################
## EKS

# Output the EKS cluster ID
output "cluster_id" {
  value = module.eks.cluster_id
}

# Returns the command needed to update the kubeconfig configuration for the EKS cluster.
output "kubeconfig_command" {
  value = "rm $HOME/.kube/config ; aws eks update-kubeconfig --name eks-triangle-env-cluster"
}

# Ouput the name of the ArgoCD Ingress service.
output "argocd_ingress_service_name" {
  value = kubernetes_ingress_v1.argocd_ingress.status.0.load_balancer.0.ingress.0.hostname
}

