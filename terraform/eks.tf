/*
  This module creates an Amazon Elastic Kubernetes Service (EKS) cluster using the terraform-aws-modules/eks/aws module.
  It provisions the EKS cluster with the specified cluster name and version, and enables public access to the cluster endpoint.
  It also enables IAM Roles for Service Accounts (IRSA) and deploys any specified cluster addons.
  The module requires the VPC module to be instantiated and provides the VPC ID and subnet IDs as inputs.
  It supports the configuration of managed node groups with the specified instance types.
*/

module "eks" {
  source  = "terraform-aws-modules/eks/aws"  # Specifies the source module for creating the EKS cluster
  version = "~> 19.17.2"  # Specifies the version of the EKS module to use

  cluster_name    = "${var.env_name}-cluster"  # Specifies the name of the EKS cluster
  cluster_version = var.cluster_version  # Specifies the version of the EKS cluster

  cluster_endpoint_public_access = true  # Enables public access to the EKS cluster endpoint
  enable_irsa                    = true  # Enables IAM Roles for Service Accounts (IRSA)

  cluster_addons = var.cluster_addons  # Specifies any additional cluster addons to deploy

  vpc_id     = module.vpc.vpc_id  # Specifies the ID of the VPC where the EKS cluster will be created
  subnet_ids = concat(sort(module.vpc.public_subnets), sort(module.vpc.private_subnets))  # Specifies the IDs of the subnets where the EKS cluster will be created

  eks_managed_node_group_defaults = {
    instance_types = var.default_instance_types  # Specifies the default instance types for the managed node groups
  }

  eks_managed_node_groups = var.eks_managed_node_groups  # Specifies the configuration for the managed node groups
}