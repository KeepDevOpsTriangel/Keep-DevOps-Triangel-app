# Metrics for the project

This values.yaml file is used to configure the metrics for the project with stack Prometheus and Grafana.
The metrics are collected from the cluster and resources Kubernetes deployed in the cluster. Also, are configured alerts to notify when the resources are in a critical state to slack channel.

## Prometheus / Grafana

The Prometheus chart is used to deploy a Prometheus server to your cluster. This chart is based on the official Prometheus Community chart. The values applied to depploy Prometheus. Including the configuration for the Prometheus server, Alertmanager, and Grafana.

To install the chart with the release name `prometheus`:

```bash
helm -n monitoring upgrade \
    --install prometheus \
    prometheus-community/kube-prometheus-stack \
    -f kube-prometheus-stack/values.yaml \
    --create-namespace \
    --wait --version 55.4.0
```

# Dashboards

The dashboards default in Grafana to visualize the metrics of the project.

# Metrics

The metrics are collected from cluster and resources Kubernetes deployed in the cluster.
Alerts are configured to notify when the resources are in a critical state to slack channel.

# Access to Grafana

To access to Grafana, you can use the following command:

```bash
kubectl -n monitoring port-forward svc/prometheus-grafana 3000:http-web
```

Then, you can access to Grafana in the following URL: [http://localhost:3000](http://localhost:3000)

The default credentials are:

- User: `admin`
- Password: `prom-operator`

# Access to Prometheus

To access to Prometheus, you can use the following command:

```bash
kubectl -n monitoring port-forward svc/prometheus-kube-prometheus-prometheus 9090:9090
```

Then, you can access to Prometheus in the following URL: [http://localhost:9090](http://localhost:9090)

>-----
> Include ingress controller to access to Grafana and Prometheus from outside the cluster, with a domain and SSL certificate.
>------