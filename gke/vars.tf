# Fichero con las variables de configuración del proyecto

variable "project_id" {
  description = "ID único del proyecto de GCP"
}

variable "credentials_file" {
  description = "Fichero JSON con las credenciales de la cuenta de servicio en GCP"
}

variable "network_name" {
  description = "Nombre de la red para la Compute Engine"
}

variable "bucket_name" {
  description = "Nombre del bucket de Cloud Storage"
}

variable "location" {
  description = "Zona de ubicación del bucket de Cloud Storage"
}

variable "region" {
  description = "Región de GCP"
}

variable "zone" {
  description = "Zona de GCP"
}

variable "name_cluster" {
  description = "Nombre del cluster de Kubernetes"
}

variable "cluster_machine_type" {
  description = "Tipo de máquina del cluster de Kubernetes"
}

variable "cluster_num_nodes" {
  description = "Número de nodos del cluster de Kubernetes"
}

variable "cluster_disk_type" {
  description = "Tipo de disco del cluster de Kubernetes"

}

variable "cluster_disk_size_gb" {
  description = "Tamaño del disco del cluster de Kubernetes"
}
