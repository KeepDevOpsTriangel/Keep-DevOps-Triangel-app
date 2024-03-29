credentials_file     = "credentials.json"
resource_name        = "triangle-app"
project_id           = "triangle-app-413819"
region               = "europe-west1"
zone                 = "europe-west1-d"
cluster_location     = "europe-west1-d"
cluster_num_nodes    = 1
cluster_machine_type = "n1-standard-1"
cluster_disk_type    = "pd-standard"
cluster_disk_size_gb = 25
argocd_chart         = "argo-cd"
argocd_repository    = "https://argoproj.github.io/argo-helm"
argocd_chart_version = "5.27.3"
argocd_file          = "../argocd/values.yaml"

