resource "random_string" "random_name" {
  length  = 5
  special = false
  upper   = false
}
resource "google_storage_bucket" "terraform_state_bucket" {
  depends_on    = [random_string.random_name]
  name          = "${var.bucket_name}-terraform-state-${random_string.random_name.result}"
  force_destroy = false
  location      = var.region
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
  uniform_bucket_level_access = true
}
