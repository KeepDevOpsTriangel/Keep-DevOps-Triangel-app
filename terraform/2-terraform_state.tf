# This Terraform configuration specifies the backend configuration for storing the Terraform state.
# The state will be stored in an S3 bucket named "bucket-eks-terraform-state" in the "eu-central-1" region.
# The state file will be named "triangle-project-state/terraform.tfstate" within the bucket.

terraform {
  backend "s3" {
    bucket = "bucket-eks-terraform-state"
    key    = "triangle-project-state/terraform.tfstate"
    region = "eu-central-1"
  }
}