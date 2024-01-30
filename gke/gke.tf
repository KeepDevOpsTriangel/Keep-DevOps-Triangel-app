resource "google_container_cluster" "primary" {
  name     = var.name_cluster
  location = var.location
  project  = var.project_id

  node_pool {
    name       = "default-pool"
    node_count = 1
    node_config {
      machine_type = var.cluster_machine_type
      disk_size_gb = var.cluster_disk_size_gb
      disk_type    = var.cluster_disk_type

      oauth_scopes = [
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring",
      ]
    }
  }
  addons_config {
    http_load_balancing {
      disabled = true
    }
  }
  master_auth {
    client_certificate_config {
      issue_client_certificate = false
    }
  }
}
