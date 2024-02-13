
resource "kubernetes_namespace" "nginx_ingress" {
    metadata {
        annotations = {
            name = "ingress-nginx"
        }
        labels = {
            env = "develop"
        }
        name = "ingress-nginx"
    }
}

resource "helm_release" "nginx-ingress-controller" {
  name       = "nginx-ingress-controller"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "nginx-ingress-controller"
  namespace  = "ingress-nginx"
  timeout    = 700 


  set {
    name  = "service.type"
    value = "LoadBalancer"
  }

  depends_on = [ kubernetes_namespace.nginx_ingress ]

}