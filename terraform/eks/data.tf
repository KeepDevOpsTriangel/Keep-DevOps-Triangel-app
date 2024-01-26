data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "bucket-eks-terraform-state"
    key    = "vpc/terraform.tfstate"
    region = "eu-central-1"
  }
}
