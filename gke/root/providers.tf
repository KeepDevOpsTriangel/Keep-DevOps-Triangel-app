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
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.25.2"
    }
    kubectl = {
      source  = "gavinbunney/kubectl"
      version = ">= 1.14.0"
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
  kubernetes {
    config_path = "~/.kube/config"
  }
}
provider "kubectl" {
  config_path = "~/.kube/config"
}
provider "kubernetes" {
  config_path = "~/.kube/config"
}
