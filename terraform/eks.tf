/*
  This module creates an Amazon Elastic Kubernetes Service (EKS) cluster using the terraform-aws-modules/eks/aws module.
  It provisions the EKS cluster with the specified cluster name and version, and enables public access to the cluster endpoint.
  It also enables IAM Roles for Service Accounts (IRSA) and deploys any specified cluster addons.
  The module requires the VPC module to be instantiated and provides the VPC ID and subnet IDs as inputs.
  It supports the configuration of managed node groups with the specified instance types.
*/

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.17.2"

  cluster_name    = "${var.env_name}-cluster"
  cluster_version = var.cluster_version

  cluster_endpoint_public_access = true
  cluster_endpoint_private_access = true
  enable_irsa                    = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = concat(sort(module.vpc.public_subnets), sort(module.vpc.private_subnets))

  cluster_addons = var.cluster_addons

 cluster_security_group_additional_rules = {
    egress_nodes_ephemeral_ports_tcp = {
      description = "Cluster API to K8S services running on nodes"
      protocol = "tcp"
      from_port = 1025
      to_port = 65535
      type = "egress"
      source_node_security_group = true
    }
  }

  node_security_group_additional_rules = {
    ingress_cluster_api_ephemeral_ports_tcp = {
      description = "Cluster API to K8S services running on nodes"
      protocol = "tcp"
      from_port = 1025
      to_port = 65535
      type = "ingress"
      source_cluster_security_group = true
    }
  }

  eks_managed_node_group_defaults = {
    instance_types = var.default_instance_types
  }

  eks_managed_node_groups = var.eks_managed_node_groups
  
}
