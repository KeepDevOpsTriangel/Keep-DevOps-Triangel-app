variable "bucket_name" {
  description = "The name of the bucket"
  type        = string
}
variable "region" {
  description = "The region to create the bucket in"
  type        = string
}
variable "storage_class" {
  description = "The storage class of the bucket"
  type        = string
  default     = "STANDARD"
}
variable "force_destroy" {
  description = "Whether to force destroy the bucket"
  type        = bool
  default     = "true"
}
variable "versioning" {
  description = "Whether to enable versioning"
  type        = bool
  default     = "true"
}
