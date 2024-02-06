######################################################################
## VPC
output "vpc_id" {
  value = module.vpc.vpc_id
}
output "private_subnets" {
  value = module.vpc.private_subnets
}

######################################################################
## EKS

output "cluster_id" {
  value = module.eks.cluster_id
}

output "kubeconfig_command" {
  value = "rm $HOME/.kube/config ; aws eks update-kubeconfig --name eks-triangle-env-cluster"
}

output "argocd_ingress_service_name" {
  value = kubernetes_ingress_v1.argocd_ingress.status.0.load_balancer.0.ingress.0.hostname
}

