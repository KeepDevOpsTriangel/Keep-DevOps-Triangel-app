variable "resource_name" {
  type        = string
  description = "resource name"
}
variable "project_id" {
  description = "unique ID of the GCP project"
}
variable "cluster_location" {
  description = "location of GCP"
}
variable "cluster_num_nodes" {
  description = "number of nodes in the cluster"
}
variable "cluster_machine_type" {
  description = "cluster machine type"
}
variable "cluster_disk_type" {
  description = "disk type of the cluster"
}
variable "cluster_disk_size_gb" {
  description = "disk size of the cluster"
}
