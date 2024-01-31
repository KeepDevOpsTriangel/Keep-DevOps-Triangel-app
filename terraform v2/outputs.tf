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
output "load_balancer_controller_iam_role_arn" {
  value = aws_iam_role.load_balancer_controller.arn
}

output "cluster_id" {
  value = module.eks.cluster_id
}

output "kubeconfig_command" {
  value = "rm $HOME/.kube/config ; aws eks update-kubeconfig --name cluster-eks-tf"
}