terraform {
  backend "gcs" {
    bucket      = "triangle-app-73vpg-tfstate"
    prefix      = "terraform/state"
    credentials = "credentials.json"
  }
}

# terraform {
#   backend "local" {
#     path = "terraform.tfstate"
#   }
# }
