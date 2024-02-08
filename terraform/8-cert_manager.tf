# This module configures the eks-cert-manager module to manage the installation and configuration of cert-manager on an EKS cluster.
module "eks-cert-manager" {
  source  = "lablabs/eks-cert-manager/aws"
  version = "1.1.1"
  cluster_identity_oidc_issuer = module.eks.cluster_oidc_issuer_url
  cluster_identity_oidc_issuer_arn = module.eks.oidc_provider_arn
  namespace = "cert-manager"
  depends_on = [ module.eks ]
}

# This resource defines the Issuer object for Let's Encrypt staging environment.
resource "kubernetes_manifest" "issuer_letsencrypt_prod" {
  manifest = {
    "apiVersion" = "cert-manager.io/v1"
    "kind" = "Issuer"
    "metadata" = {
      "name" = "letsencrypt-prod"
      "namespace" = "cert-manager"
    }
    "spec" = {
      "acme" = {
        "email" = "jeffnacato@gmail.com"
        "privateKeySecretRef" = {
          "name" = "letsencrypt-prod"
        }
        "server" = "https://acme-v02.api.letsencrypt.org/directory"
        "solvers" = [
          {
            "http01" = {
              "ingress" = {
                "ingressClassName" = "nginx"
              }
            }
          },
        ]
      }
    }
  }
}