data "http" "argo_cd_install_yaml" {
  url = "https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml"
}
resource "kubernetes_manifest" "argocd_install" {
  manifest = data.http.argo_cd_install_yaml.body
}
