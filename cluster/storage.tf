# Function to ramdomly generate a string for the unique bucket name
resource "random_string" "random" {
  length  = 5
  special = false
  upper   = false
}
resource "google_storage_bucket" "tfstate" {
  name          = "${var.resource_name}-${random_string.random.result}-tfstate"
  location      = var.region
  force_destroy = true

  lifecycle_rule {
    condition {
      num_newer_versions = 5
    }
    action {
      type = "Delete"
    }
  }
  versioning {
    enabled = true
  }
}
