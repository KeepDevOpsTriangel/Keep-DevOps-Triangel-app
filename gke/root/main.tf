module "gke" {
  source               = "../modules/gke"
  resource_name        = var.resource_name
  project_id           = var.project_id
  cluster_location     = var.zone
  cluster_num_nodes    = 1
  cluster_machine_type = "n1-standard-1"
  cluster_disk_type    = "pd-standard"
  cluster_disk_size_gb = 25
}
