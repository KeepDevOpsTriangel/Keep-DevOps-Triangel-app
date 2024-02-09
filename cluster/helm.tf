resource "kubernetes_namespace" "argocd" {
  depends_on = [google_container_cluster.devcluster]
  metadata {
    name = "argocd"
  }
}
resource "helm_release" "argocd" {
  depends_on = [kubernetes_namespace.argocd, google_container_cluster.devcluster]
  name       = "${var.resource_name}-argocd"
  chart      = var.chart
  repository = var.repository
  namespace  = "argocd"
  version    = var.chart_version
  timeout    = "1200"
  values     = [templatefile("${var.file}", {})]
}
