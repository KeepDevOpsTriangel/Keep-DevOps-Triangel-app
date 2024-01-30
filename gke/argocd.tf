resource "helm_release" "argo_cd" {
  name       = "argo-cd"
  repository = "https://argoproj.github.io/argo-helm"
  chart      = "argo-cd"
  namespace  = "argo"

  set {
    name  = "server.service.type"
    value = "LoadBalancer"
  }
}

resource "google_compute_firewall" "argo_cd_fw" {
  name    = "allow-argo-cd-ingress"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}
