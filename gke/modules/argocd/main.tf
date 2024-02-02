resource "kubernetes_namespace" "argocd" {
  metadata {
    name = var.namespace
  }
}
resource "helm_release" "argocd" {
  depends_on = [kubernetes_namespace.argocd]
  name       = "${var.resource_name}-argocd"
  chart      = var.chart
  repository = var.repository
  namespace  = var.namespace
  version    = var.chart_version
  timeout    = "1200"
  values     = [templatefile("${var.file}", {})]
}
