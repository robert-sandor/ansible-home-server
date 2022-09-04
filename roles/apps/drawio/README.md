# Cyberchef

[Draw.io](https://www.diagrams.net/) (also known as Diagrams.net) is an open source technology stack for building diagramming applications, and the world’s most widely used browser-based end-user diagramming software.

## Configuration

- `drawio_version`
    - Default: `latest`
    - Version of Draw.io to deploy. For available versions check [DockerHub](https://hub.docker.com/r/jgraph/drawio/tags).
- `drawio_export_version`
    - Default: `latest`
    - Version of Draw.io export container to deploy. For available versions check [DockerHub](https://hub.docker.com/r/jgraph/export-server/tags).
- `drawio_plantuml_version`
    - Default: `latest`
    - Version of Draw.io PlanUML container to deploy. For available versions check [DockerHub](https://hub.docker.com/r/jgraph/plantuml-server/tags).
- `drawio_network`
    - Default: `apps`
    - Docker network to add Draw.io to.
