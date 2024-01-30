# Inicializamos las librerías de Terraform para Google Cloud Platform
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.81.0"
    }
  }
}

# Configuramos el proveedor de Google Cloud Platform
provider "google" {
  # Indicamos el archivo JSON de la cuenta de servicio
  credentials = file(var.credentials_file)
  # Indicamos el proyecto y la región y la zona
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Función para generar un string aleatorio
resource "random_string" "random" {
  length  = 5
  special = false
  upper   = false
}


