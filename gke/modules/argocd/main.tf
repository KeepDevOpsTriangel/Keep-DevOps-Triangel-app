resource "helm_release" "argocd" {
  name       = "${var.resource_name}-argocd"
  repository = var.chart_repository
  chart      = var.chart_name
  values = [
    file("../modules/argocd/values.yaml")
  ]
}

# resource "google_compute_firewall" "argo_cd_fw" {
#   name    = "allow-argo-cd-ingress"
#   network = "default"

#   allow {
#     protocol = "tcp"
#     ports    = ["80", "443"]
#   }

#   source_ranges = ["0.0.0.0/0"]
# }
