resource "random_string" "random_name" {
  length  = 5
  special = false
  upper   = false
}
resource "google_storage_bucket" "terraform_state_bucket" {
  depends_on    = [random_string.random_name]
  name          = "${var.bucket_name}-terraform-state"
  force_destroy = var.force_destroy
  location      = var.region
  storage_class = var.storage_class
  versioning {
    enabled = var.versioning
  }
  uniform_bucket_level_access = true
}
# resource "google_storage_bucket" "terraform_state_bucket_local" {
#   name                        = "${var.bucket_name}-terraform-state-local"
#   location                    = var.region
#   uniform_bucket_level_access = true
# }
