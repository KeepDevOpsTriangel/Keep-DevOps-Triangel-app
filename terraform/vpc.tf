# This Terraform code defines the configuration for creating a VPC (Virtual Private Cloud) in AWS.
# It uses the terraform-aws-modules/vpc/aws module to provision the VPC resources.

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

  # Name of the VPC
  name = "${var.name_prefix}-vpc"

  # CIDR block for the VPC
  cidr = var.vpc_cidr

  # Availability Zones for the VPC subnets
  azs             = local.azs

  # CIDR blocks for the public subnets
  public_subnets  = local.public_subnets_list_cidr

  # CIDR blocks for the private subnets
  private_subnets = local.private_subnets_list_cidr

  # Tags for the public subnets
  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }

  # Tags for the private subnets
  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }

  # Enable NAT gateway for private subnets
  enable_nat_gateway      = true

  # Use a single NAT gateway for all private subnets
  single_nat_gateway      = true

  # Enable VPN gateway
  enable_vpn_gateway      = true

  # Create an Internet Gateway
  create_igw              = true

  # Automatically assign public IP addresses to instances launched in public subnets
  map_public_ip_on_launch = true
}

