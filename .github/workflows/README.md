# CI/CD - Workflows

Este README proporciona una visión general de los flujos de trabajo disponibles en este repositorio. Cada trabajo está diseñado para realizar una tarea específica en el proceso de desarrollo y entrega del software. Para obtener más detalles sobre cada trabajo y sus configuraciones, consulte los archivos de flujo de trabajo individuales en el directorio [.github/workflows/](.github/workflows/) del repositorio.

## Pipeline test_and_docs

Este [workflow](/.github/workflows/test_and_docs.yml) consta de 3 jobs principales, en los que su función será testear y documentar nuestra aplicación.

1. Testing-and-sonarcloud:
    - Primero configuramos unas variables para levantar una db mysql. Dicha db sería usada posteriormente para que el equipo de desarrollo pueda implementar más tests si fuera necesario.
    - Se instalan todas las dependencias necesarias, ubicadas en [requirements.txt](/app/requirements.txt) y se ejecuta el contenedor de MYSQL usando también un [script](/app/tools/check_mysql_ready.sh) que verifica cuando estará dispnible la base de datos.
    - Se generan tests unitarios, ubicados en [test_app.py](/app/src/tests/test_app.py) y un informe de cobertura del código el cual será necesario para que SonarCloud pueda ejecutarse.
    - Se ejecuta un linting con Pylint, en este caso usamos un umbral bajo (under=1.0), por no disponer de equipo de desarrollo que pueda verificar el código completo y eliminamos el contenedor MYSQL creado anteriormente.
    - Finalizamos el primer job con una llamada a SonarCloud para que pueda analizar el código completo, su cobertura, calidad, errores, etc... Al terminar este paso se muestra un output con la URL del proyecto en Sonar --> [SonarCloud-TriangleApp](https://sonarcloud.io/project/overview?id=KeepDevOpsTriangel_Keep-DevOps-Triangel-app)
        - En estos momentos hemos añadido un Gate Quality personalizado en SonarCloud, debido a la gran cantidad de código y el poco coverage que nos dan los tests unitarios. El equipo de desarrollo estaría a cargo de crear o modificar los tests para así llegar a un buen índice de coverage.

2. Snyk:
    - Este trabajo ejecuta un análisis de vulnerabilidades en el código utilizando Snyk. Únicamente se ejecutará si el job anterior es exitoso.
    - Al terminar, muestra un output con las vulnerabilidades de las librerias y dependencias usadas en el código, por su hubiera un posible fallo de seguridad o versiones que ya están deprecadas.
    - Para revisar los informes de seguridad del proyecto en Snyk se puede acceder en [Snyk TriangleApp](https://app.snyk.io/org/keepdevopstriangel?fromGitHubAuth=true)

3. Generate-docs:
    - La principal función de ese trabajo es generar documentación para el proyecto y archivarla como artefacto, todo ello usando la herramienta pdoc.
    -  Del mismo modo que su predecesor, sólo se ejecuta cuando los jobs anteriores terminen sin errores, ya que generar una documentación de un código erróneo o con vulnerabilidades destacables no tendría mucho sentido.
    - Dicha documentación es accesible a través de la interfaz de GHA, tal como se muestra en la siguiente imagen:

        ![Artifact_docs](/doc_images/docs-artifact.png)


## Pipeline release

Este [workflow](/.github/workflows/release.yml) consta de un único job que se encarga de construir y publicar nuestra aplicación, tanto en Github Container Registry como en Dockerhub.

- Utilizamos un sistema de versionado mediante etiquetado manual, con esto logramos tener un control más directo y mayor flexibilidad sobre los procesos del versionado para adaptar dichas versiones a las necesidades especificas del proyecto.
- Con este sistema de etiquetado tambien nos ahorramos depender de herramientas de terceros como lo es Semantic-Release.
- Se está valorando, en un futuro, implementar un sistema de versionado más automatizado.

### Funcionamiento versionado por etiquetas

En este repositorio usamos el criterio más estandarizado para versionar todas las releases que se van lanzando, "Semver". Para resumirlo brevemente, los dígitos de las etiquetas de cada versión se relacionan con el cambio que se ha hecho en la aplicación.
En términos generales, un correcto versionado sería el siguiente:


   ![versionado](/doc_images\semver.png)


- Pequeña modificación, arreglos de bugs, etc... 
    - Se cambiará el último dígito (PATCH o FIX).
- Modificación moderada, se pueden incluir nuevas funcionalidades pero no incluye cambios drásticos de dependencias.
    - Se cambiará el dígito del medio (MINOR o FEAT).
- Modificación del código severa, cambia gran parte de dependencias y la versión de las mismas (nuevas apis, etc...).
    - Se cambiará el primer dígito (MAJOR o BREAKING CHANGE).

Para poder versionar una nueva release es obligatorio que la etiqueta empiece por "v". De ese modo, si quisieramos lanzar una nueva versión, en la que hemos arreglado algún bug, estando ahora en la v1.0.0, el tag debería ser similar a esto:

```
git tag -a v1.0.1 -m "Versión 1.0.1, modificado script XXX" # Esto crear una nueva etiqueta.
git push origin v1.0.1  # Ahora empuja la nueva etiqueta al remoto y se publica esa versión.
```

Asimismo también se pueden eliminar etiquetas, por si hubiera algun error de transcripción. En el siguiente ejemplo se puede observar como eliminamos una etiqueta mal escrita, para corregirla y publicar la correcta.

```
git tag -d v1.1.0.veta  # Eliminar etiqueta localmente
git push origin :refs/tags/v1.1.0.veta  # Eliminar etiqueta en el remoto
git tag -a v1.1.0.beta -m "Versión 1.1.0.beta"  # Crear nueva etiqueta localmente
git push origin v1.1.0.beta  # Empujar nueva etiqueta al remoto
```

Como hemos mencionado anteriormente, este pipeline sólo consta de un job:

- Build-publish-Docker-image:
    - En el mismo job le damos permisos de lectura y escritura, esto sólo lo hará en ese job, sería semejante a crear token de Github con esos permisos.
    - Para los pasos posteriores son necesarios algunos secrets, almacenados en la interfaz de github, concretamente en el apartado secrets de Github Actions.
    [Settings >> Secrets and variables >> Actions >> Secrets]
    - Finalmente se genera y se publica la imagen Docker de nuestra aplicación, tanto en GHCR como en Dockerhub. Se puede acceder a ella a través de las siguientes URL:
        - [Docker TriangleApp](https://hub.docker.com/repository/docker/kctriangle/triangle-bot/general)
        - [GHCR](https://github.com/KeepDevOpsTriangel/Keep-DevOps-Triangel-app/pkgs/container/keep-devops-triangel-app)






