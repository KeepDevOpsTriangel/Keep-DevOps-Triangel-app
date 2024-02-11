terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~>5.14.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.25.2"
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
provider "kubernetes" {
  host                   = "https://${google_container_cluster.devcluster.endpoint}"
  cluster_ca_certificate = base64decode(google_container_cluster.devcluster.master_auth[0].cluster_ca_certificate)
  token                  = data.google_client_config.current.access_token
}
provider "helm" {
  kubernetes {
    host                   = google_container_cluster.devcluster.endpoint
    token                  = data.google_client_config.current.access_token
    client_certificate     = base64decode(google_container_cluster.devcluster.master_auth.0.client_certificate)
    client_key             = base64decode(google_container_cluster.devcluster.master_auth.0.client_key)
    cluster_ca_certificate = base64decode(google_container_cluster.devcluster.master_auth.0.cluster_ca_certificate)
  }
}
