# Keep-DevOps-Triangel-app

Repositorio para el proyecto final del curso de DevOps and Cloud Computing VIII de KeepCoding.

# Equipo de Trabajo

- [Yuldor Librán](https://github.com/YuldiKeepCoding)
- [Albert Fernández](https://github.com/albertferal)
- [Jeff](https://github.com/jeffersonnc)
- [Rafael Torices](https://github.com/RafaTorices)

# Descripción del proyecto

El proyecto consiste en el desarrollo de una aplicación de chatbot integrada con Telegram y ChatGPT que permite a los usuarios interactuar con un bot inteligente capaz de comprender y generar respuestas relevantes en función de la conversación y del contexto pre-definido del Bot.
La aplicación se ha desarrollado con Python y se han usado distintas librerías como Flask para el panel web del admin de la app. Se hacen uso de las Api de Telegram para el Bot y de la Api de OpenAI para el uso de chatgpt en el Bot.
La aplicación hace uso de bases de datos Redis (para el login web), MySQL para almacenar los usuarios y opciones del Bot y MongoDB para almacenar los messages intercambiados con el chatbot.
Para el despliegue de la aplicación se dispone de un Helm Chart que incluye el despliegue de todos los componentes de la app. Además se ha utilizado ArgoCD para automatizar el despliegue continuo y asegurar la disponibilidad de la app. Se han definido dos pipelines con sus workflows correspondientes: uno para el testeo, análisis de código y generación de la documentación de la app y otro para la construcción y publicación de la imagen de la app en el repositorio de DockerHub. Para la puesta en producción de la app se han utilizado dos clúster distintos, uno en AWS y otro en GKE con el objetivo de poner en práctica lo aprendido en cuanto a infraestructura. Se ha utilizado Terraform en ambos casos para la disposición de esa infraestructura.

# Proyecto en ejecución

[Bot Telegram App](https://t.me/TriangleAppBot) (https://t.me/TriangleAppBot)

[Panel web admin](https://triangleapp.rafaeltorices.com/) (https://triangleapp.rafaeltorices.com/)

[ArgoCD](https://argocdtriangleapp.rafaeltorices.com/argocd/) (https://argocdtriangleapp.rafaeltorices.com/argocd/)


# Ciclo de integración continua

![alt text](/doc_images/devops.png)

# Esquema Aplicación

![Alt text](/doc_images/triangle-app-app.png)


# Tecnologías utilizadas

![alt text](/doc_images/keep-project.png)

# Documentación del proyecto

## Aplicación

- [Aplicación Python-Flask](app/Readme.md)

## Entorno de desarrollo

- [Docker](#)
- [Docker Compose](#)

## Entorno de producción

- [EKS](/)
- [GKE](/cluster/Readme.md)
- [Helm Charts](/helm/Readme.md)
- [ArgoCD](/argocd/Readme.md)
- [Kubernetes](/k8s/Readme.md)

## CI-CD

[GitHub Actions](.github/workflows/README.md)

# Otros recursos utilizados

    - Ingress Controller Nginx (Ingress para Argocd y App)

    - Cert-Manager (Certificados SSL para Argocd y App)

    - Issuers de Let's Encrypt para los certificados https
    
    - Sealed Secret (para encriptación de secrets tokens en el cluster)

# Fuentes de información

- [Documentación de AWS](https://docs.aws.amazon.com/es_es/)
- [Documentación de Docker](https://docs.docker.com/)
- [Documentación de Docker Compose](https://docs.docker.com/compose/)
- [Documentación de Terraform](https://www.terraform.io/docs/index.html)
- [Documentación de Helm](https://helm.sh/docs/)
- [Documentación de ArgoCD](https://argo-cd.readthedocs.io/en/stable/)
- [Documentación de CircleCI](https://circleci.com/docs/)
- [Documentación de GitHub Actions](https://docs.github.com/es/actions)
- [Documentación de Prometheus](https://prometheus.io/docs/introduction/overview/)
- [Documentación de Grafana](https://grafana.com/docs/grafana/latest/)
- [Documentación de Ansible](https://docs.ansible.com/ansible/latest/index.html)
- [Documentación de Kubernetes](https://kubernetes.io/docs/home/)
- [Documentación de Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Documentación de MySQL](https://dev.mysql.com/doc/)
- [Documentación de Python](https://docs.python.org/3/)


