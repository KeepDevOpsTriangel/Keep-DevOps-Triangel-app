variable "resource_name" {
  description = "resource name"
  type        = string
}
variable "project_id" {
  description = "unique ID of the GCP project"
  type        = string
}
variable "credentials_file" {
  description = "JSON file with the credentials of the service account in GCP"
  type        = string
}
variable "region" {
  description = "Region of GCP"
  type        = string
}
variable "zone" {
  description = "zone of GCP"
  type        = string
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
variable "argocd_chart" {
  type = string
}
variable "argocd_repository" {
  type = string
}
variable "argocd_chart_version" {
  type = string
}
variable "argocd_file" {
  type = string
}
