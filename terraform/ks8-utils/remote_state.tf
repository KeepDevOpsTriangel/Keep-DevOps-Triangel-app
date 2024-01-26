terraform {
  backend "s3" {
    bucket = "bucket-eks-terraform-state"
    key    = "ks8-utils/terraform.tfstate"
    region = "eu-central-1"
  }
}