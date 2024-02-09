data "google_client_config" "current" {}
resource "google_container_cluster" "devcluster" {
  name                = "${var.resource_name}-cluster"
  project             = var.project_id
  location            = var.cluster_location
  deletion_protection = false
  node_pool {
    name       = "${var.resource_name}-cluster-nodes"
    node_count = var.cluster_num_nodes
    node_config {
      machine_type = var.cluster_machine_type
      disk_type    = var.cluster_disk_type
      disk_size_gb = var.cluster_disk_size_gb

      oauth_scopes = [
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring",
      ]
    }
  }
}
