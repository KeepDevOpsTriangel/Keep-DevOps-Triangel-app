# This Terraform code defines the configuration for creating a VPC (Virtual Private Cloud) in AWS.
# It uses the terraform-aws-modules/vpc/aws module to provision the VPC resources.

locals {
  azs         = ["${var.aws_region}a", "${var.aws_region}b", "${var.aws_region}c"]  # Defines the availability zones for the VPC subnets
  num_of_az   = length(local.azs)  # Calculates the number of availability zones
  subnet_cidr = cidrsubnets(var.vpc_cidr, var.public_subnets_cidr_root_newbits, var.private_subnets_cidr_root_newbits)  # Calculates the CIDR blocks for the subnets
}

locals {
  public_subnets_list_cidr  = cidrsubnets(local.subnet_cidr[0], [for i in range(local.num_of_az) : var.public_subnets_cidr_sub_newbits]...)  # Calculates the CIDR blocks for the public subnets
  private_subnets_list_cidr = cidrsubnets(local.subnet_cidr[1], [for i in range(local.num_of_az) : var.private_subnets_cidr_sub_newbits]...)  # Calculates the CIDR blocks for the private subnets
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"  # Specifies the source module for creating the VPC

  name = "${var.name_prefix}-vpc"   # Name of the VPC

  cidr = var.vpc_cidr 

  azs             = local.azs   # Availability Zones for the VPC subnets


  public_subnets  = local.public_subnets_list_cidr  # CIDR blocks for the public subnets


  private_subnets = local.private_subnets_list_cidr   # CIDR blocks for the private subnets

  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1   # Tags for the public subnets
  }

  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1   # Tags for the private subnets
  }

  enable_nat_gateway      = true   # Enable NAT gateway for private subnets

  single_nat_gateway      = true   # Use a single NAT gateway for all private subnets

  enable_vpn_gateway      = true   # Enable VPN gateway

  create_igw              = true   # Create an Internet Gateway

  map_public_ip_on_launch = true   # Automatically assign public IP addresses to instances launched in public subnets
}

