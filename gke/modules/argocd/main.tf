resource "helm_release" "argocd" {
  name = "${var.resource_name}-argocd"
  #   repository = "https://argoproj.github.io/argo-helm"
  #   chart      = "argocd"
  #   version    = "5.53.12"
  repository = var.chart_repository
  chart      = var.chart_name
  version    = var.chart_version

  values = [
    "${file("values.yaml")}"
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
