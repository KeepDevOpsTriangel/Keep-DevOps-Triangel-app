output "IP_address_nginx_controller" {
  value       = google_compute_address.ingress_ip_address.address
  description = "IP address of the ingress controller"
}
output "argocd_password" {
  value = local_file.argocd_password.content
}
