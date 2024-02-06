module "eks-cert-manager" {
  source  = "lablabs/eks-cert-manager/aws"
  version = "1.1.1"
  cluster_identity_oidc_issuer = module.eks.cluster_oidc_issuer_url
  cluster_identity_oidc_issuer_arn = module.eks.oidc_provider_arn
  namespace = "cert-manager"
  depends_on = [ module.eks ]
  
}

resource "kubernetes_manifest" "issuer_letsencrypt_staging" {
  manifest = {
    "apiVersion" = "cert-manager.io/v1"
    "kind" = "Issuer"
    "metadata" = {
      "name" = "letsencrypt-staging"
      "namespace" = "cert-manager"
    }
    "spec" = {
      "acme" = {
        "email" = "jeffnacato@gmail.com"
        "privateKeySecretRef" = {
          "name" = "letsencrypt-staging"
        }
        "server" = "https://acme-staging-v02.api.letsencrypt.org/directory"
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
  depends_on = [ module.eks-cert-manager ]
}