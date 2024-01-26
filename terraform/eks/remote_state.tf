terraform {
  backend "s3" {
    bucket = "bucket-eks-terraform-state"
    key    = "eks/terraform.tfstate"
    region = "eu-central-1"
  }
}