# EKS infrastructure by Terraform
This repository includes the required Terraform files to provision following components,
- Single node group EKS cluster 
- AWS Load Balancer Controller
- ArgoCD server exposed by AWS Application Load Balancer



# Usage
1. Open the terminal and run aws configure. Follow the prompts and input your credentials.
```
aws configure

    acces key: 
    Secret access key:
```

2. Initialize terraform dependencies by,
```
terraform init
```
3. Get the list of resources being created by,
```
terraform plan
```
5. Create the planned resources by,
```
terraform apply
```

despues de desplegar el cluster de eks, se tiene que descomentar el resource "kubernetes_manifest" "issuer_letsencrypt_prod" de  8-cert-manager.tf

## Outputs

- `argocd_ingress_service_name`: This is the URL through which ArgoCD can be accessed.


- `kubeconfig_command`: The command to update the kubeconfig file for the dev-cluster.

- `comaand pass` : kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d


# Terraform Code

# Módulo VPC

### Locales

Se definen dos bloques `locals`. El primer bloque define las zonas de disponibilidad (AZs) basándose en la región de AWS proporcionada, calcula el número de AZs y genera las subredes CIDR.

El segundo bloque de `locals` genera las listas de subredes CIDR para las subredes públicas y privadas.

El módulo `vpc` utiliza el módulo VPC de la comunidad de Terraform para AWS. Aquí se definen las siguientes variables:

- `name`: El nombre de la VPC, que se genera a partir del prefijo de nombre proporcionado.
- `cidr`: El bloque CIDR para la VPC.
- `azs`: Las zonas de disponibilidad para la VPC.
- `public_subnets`: Los bloques CIDR para las subredes públicas.
- `private_subnets`: Los bloques CIDR para las subredes privadas.
- `public_subnet_tags`: Las etiquetas para las subredes públicas.
- `private_subnet_tags`: Las etiquetas para las subredes privadas.

Además, se habilitan varias características de la VPC, como la puerta de enlace NAT, la puerta de enlace VPN, la puerta de enlace de Internet y el mapeo de IP pública en el lanzamiento.

# Módulo IAM Role

El módulo `lbc_role` crea un rol de IAM para el controlador de balanceador de carga. Este rol se adjunta a la política del controlador de balanceador de carga y se configura con un proveedor OIDC que permite al controlador de balanceador de carga interactuar con otros servicios de AWS.

### Recurso de la cuenta de servicio de Kubernetes

El recurso `kubernetes_service_account` crea una cuenta de servicio de Kubernetes para el controlador de balanceador de carga. Esta cuenta de servicio se etiqueta y se anota con el ARN del rol de IAM creado anteriormente.

### Recurso de lanzamiento de Helm

El recurso `helm_release` instala el controlador de balanceador de carga en el clúster de Kubernetes utilizando Helm. Se configura con varios valores, incluyendo la región de AWS, el ID de la VPC, el repositorio de imágenes y el nombre de la cuenta de servicio de Kubernetes. También se establece una dependencia en la cuenta de servicio de Kubernetes para asegurar que se crea antes de que se instale el controlador de balanceador de carga.

# Backend de Terraform

El backend de Terraform se utiliza para almacenar el estado de Terraform. El estado de Terraform es un archivo JSON que contiene la representación de los recursos que Terraform ha creado y está gestionando.

En este script, se configura un backend S3 para almacenar el estado de Terraform. Los detalles del backend S3 son los siguientes:

- `bucket`: El nombre del bucket S3 donde se almacenará el estado de Terraform. En este caso, el bucket se llama "bucket-eks-terraform-state".
- `key`: La clave del archivo de estado de Terraform en el bucket S3. En este caso, la clave es "triangle-project-state/terraform.tfstate".
- `region`: La región de AWS donde se encuentra el bucket S3. En este caso, la región es "eu-central-1".


el backend se debe crear sea de forma manual en consola antes de ejecutar `terraform plan`


# Módulo EKS

El módulo `eks` utiliza el módulo EKS de la comunidad de Terraform para AWS. Aquí se definen las siguientes variables:

- `cluster_name`: El nombre del clúster de EKS, que se genera a partir del nombre del entorno proporcionado.
- `cluster_version`: La versión del clúster de EKS.
- `cluster_endpoint_public_access` y `cluster_endpoint_private_access`: Estos parámetros controlan el acceso público y privado al punto final del clúster de EKS.
- `enable_irsa`: Habilita el servicio de cuentas de IAM para los pods de servicio.
- `vpc_id` y `subnet_ids`: La ID de la VPC y las IDs de las subredes donde se desplegará el clúster de EKS.
- `cluster_addons`: Los complementos del clúster de EKS.
- `cluster_security_group_additional_rules` y `node_security_group_additional_rules`: Reglas adicionales de seguridad para el clúster y los nodos.
- `eks_managed_node_group_defaults`: Los tipos de instancias por defecto para los grupos de nodos gestionados por EKS.
- `eks_managed_node_groups`: Los grupos de nodos gestionados por EKS.

# Nginx Ingress Controller

### Recurso del Namespace de Kubernetes

El recurso `kubernetes_namespace` crea un namespace en Kubernetes llamado "ingress-nginx". Este namespace se anota y se etiqueta para su uso con el controlador de Ingress Nginx.

### Recurso de lanzamiento de Helm

El recurso `helm_release` despliega el controlador de Ingress Nginx en el namespace "ingress-nginx" utilizando Helm. El controlador de Ingress Nginx se configura para exponerse a través de un LoadBalancer.

El recurso `helm_release` depende del recurso `kubernetes_namespace`, lo que significa que el namespace "ingress-nginx" se creará antes de que se despliegue el controlador de Ingress Nginx.

# Argocd

### Recurso del Namespace de Kubernetes

El recurso `kubernetes_namespace_v1` crea un namespace en Kubernetes para ArgoCD. El nombre del namespace se obtiene de la variable `argocd_target_namespace`.

### Recurso de lanzamiento de Helm

El recurso `helm_release` despliega ArgoCD en el namespace especificado utilizando Helm. Se configura con varios valores, incluyendo el nombre del despliegue, la URL del repositorio de Helm, el nombre del chart de Helm, y si se debe limpiar en caso de fallo. También se establece una configuración para ejecutar el servidor sin TLS.

### Recurso de Ingress de Kubernetes

El recurso `kubernetes_ingress_v1` crea un Ingress para ArgoCD. Este Ingress se configura para utilizar el controlador de Ingress ALB y para dirigir el tráfico al servicio "argocd-server" en el puerto 80.

# Cert Manager

### Módulo cert-manager

El módulo `eks-cert-manager` utiliza el módulo cert-manager de la comunidad de Terraform para AWS. Se configura con la URL del emisor OIDC del clúster y el ARN del proveedor OIDC, así como el namespace en el que se desplegará cert-manager.

### Recurso del emisor de certificados

El recurso `kubernetes_manifest` define un objeto Issuer para el entorno de producción de Let's Encrypt. Este emisor se configura con un correo electrónico y una referencia a un secreto para la clave privada. También se configura para utilizar el servidor de producción de Let's Encrypt y para resolver los desafíos ACME utilizando el método HTTP01 con el controlador de Ingress Nginx.

# Outputs

### Salida de la ID de la VPC

La salida `vpc_id` devuelve la ID de la VPC creada por el módulo `vpc`.

### Salidas de EKS

La salida `cluster_id` devuelve la ID del clúster de EKS creado por el módulo `eks`.

La salida `kubeconfig_command` devuelve el comando necesario para actualizar la configuración de kubeconfig para el clúster de EKS. Este comando elimina la configuración existente de kubeconfig y luego utiliza el comando `aws eks update-kubeconfig` para crear una nueva configuración para el clúster de EKS.

### Salida del nombre del servicio de Ingress de ArgoCD

La salida `argocd_ingress_service_name` devuelve el nombre del servicio de Ingress para ArgoCD. Este nombre se obtiene del estado del recurso `kubernetes_ingress_v1` para el Ingress de ArgoCD.

# Providers

Este archivo `provider.tf` es un script de Terraform que define los proveedores que se utilizarán en los módulos de Terraform. Los proveedores son las interfaces a los servicios que Terraform utilizará para gestionar los recursos.

# Proveedor AWS

El proveedor `aws` se configura con la región de AWS, la ruta al archivo de credenciales compartidas de AWS y el perfil de las credenciales de AWS. También se configuran las etiquetas por defecto que se aplicarán a todos los recursos creados por este proveedor.

### Proveedor Kubernetes

El proveedor `kubernetes` se configura con el punto final del clúster de EKS, el certificado de autoridad del clúster y un bloque `exec` que define cómo obtener un token de autenticación para el clúster. Este bloque `exec` requiere que el AWS CLI esté instalado localmente donde se ejecuta Terraform.

## Proveedor Helm

El proveedor `helm` se configura de manera similar al proveedor `kubernetes`, pero se utiliza para interactuar con Helm, una herramienta para desplegar aplicaciones en Kubernetes.









