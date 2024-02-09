terraform {
  backend "gcs" {
    bucket      = "triangle-app-j3sbk-tfstate"
    prefix      = "terraform/state"
    credentials = "credentials.json"
  }
}

# terraform {
#   backend "local" {
#     path = "terraform.tfstate"
#   }
# }
