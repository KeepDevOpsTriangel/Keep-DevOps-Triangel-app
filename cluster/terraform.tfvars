credentials_file     = "credentials_triangleapp_dev.json"
resource_name        = "botdemo"
project_id           = "botdemo-413810"
region               = "europe-west1"
zone                 = "europe-west1-d"
cluster_location     = "europe-west1-d"
cluster_num_nodes    = 1
cluster_machine_type = "n1-standard-1"
cluster_disk_type    = "pd-standard"
cluster_disk_size_gb = 25
chart                = "argo-cd"
repository           = "https://argoproj.github.io/argo-helm"
chart_version        = "5.27.3"
file                 = "values.yaml"

