terraform {
  backend "local" {
    path = "terraform/state/terraform.tfstate"
  }
}
# terraform {
#   backend "gcs" {
#     bucket = "bottelegram-terraform-state-terraform-state"
#     prefix = "terraform/state"
#   }
# }
