# This Terraform configuration file defines providers for AWS, Kubernetes, and Helm.
# The AWS provider is used to interact with AWS services, such as EC2 instances and S3 buckets.
# The Kubernetes provider is used to manage resources in a Kubernetes cluster.
# The Helm provider is used to install and manage Helm charts in a Kubernetes cluster.

provider "aws" {
  region                   = var.aws_region
  shared_credentials_files = ["${var.aws_cred_file_path}"]
  profile                  = var.aws_cred_profile

  default_tags {
    tags = {
      provision-by = var.provisioner
      env          = var.env_name
    }
  }
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    # This requires the awscli to be installed locally where Terraform is executed
    args = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
  }
}

provider "helm" {
  kubernetes {
    host                   = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      args        = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
      command     = "aws"
    }
  }
}