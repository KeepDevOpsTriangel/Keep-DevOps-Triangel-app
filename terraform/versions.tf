# This file specifies the required providers for the Terraform configuration.
# It ensures that the correct version of the AWS provider is used.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.23.1"
    }
  }
}