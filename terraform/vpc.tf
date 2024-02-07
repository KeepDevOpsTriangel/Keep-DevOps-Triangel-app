# This Terraform code defines the configuration for the VPC (Virtual Private Cloud) module.
# It creates a VPC with public and private subnets across multiple availability zones (AZs).
# The VPC is configured with NAT gateways, VPN gateway, and an internet gateway (IGW).
# Public subnets are tagged with "kubernetes.io/role/elb" and private subnets are tagged with "kubernetes.io/role/internal-elb".
# The VPC module is sourced from the "terraform-aws-modules/vpc/aws" module.


locals {
  azs         = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]
  num_of_az   = length(local.azs)
  subnet_cidr = cidrsubnets(var.vpc_cidr, var.public_subnets_cidr_root_newbits, var.private_subnets_cidr_root_newbits)
}

locals {
  public_subnets_list_cidr  = cidrsubnets(local.subnet_cidr[0], [for i in range(local.num_of_az) : var.public_subnets_cidr_sub_newbits]...)
  private_subnets_list_cidr = cidrsubnets(local.subnet_cidr[1], [for i in range(local.num_of_az) : var.private_subnets_cidr_sub_newbits]...)
}


module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "${var.name_prefix}-vpc"
  cidr = var.vpc_cidr

  azs             = local.azs
  public_subnets  = local.public_subnets_list_cidr
  private_subnets = local.private_subnets_list_cidr

  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }

  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }

  enable_nat_gateway      = true
  single_nat_gateway      = true
  enable_vpn_gateway      = true
  create_igw              = true
  map_public_ip_on_launch = true
}