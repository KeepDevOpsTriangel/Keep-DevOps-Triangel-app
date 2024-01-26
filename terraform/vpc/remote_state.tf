terraform {
  backend "s3" {
    bucket = "bucket-eks-terraform-state"
    key    = "vpc/terraform.tfstate"
    region = "eu-central-1"
  }
}