terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~>5.14.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~>2.12.1"
    }
  }
}
provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project_id
  region      = var.region
  zone        = var.zone
}
provider "helm" {
}
