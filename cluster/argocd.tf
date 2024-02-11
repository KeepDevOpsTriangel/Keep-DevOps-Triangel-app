resource "kubernetes_namespace" "argocd" {
  depends_on = [google_container_cluster.devcluster]
  metadata {
    name = "argocd"
  }
}
resource "helm_release" "argocd" {
  depends_on = [kubernetes_namespace.argocd, google_container_cluster.devcluster]
  name       = "${var.resource_name}-argocd"
  chart      = var.argocd_chart
  repository = var.argocd_repository
  namespace  = "argocd"
  version    = var.argocd_chart_version
  timeout    = "1200"
  values     = [templatefile("${var.argocd_file}", {})]
}
