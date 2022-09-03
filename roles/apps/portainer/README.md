# Portainer

[Portainer](https://www.portainer.io/?hsLang=en) is a tool used to managed docker, docker swarm and kubernetes clusters. 
It can be used to have access to all deployed services, logs, etc. 
This playbook uses the Community Edition of Portainer.

Once deployed, the service will be available on port `9000`, and if a reverse proxy is also installed, it will be available at `portainer.<domain>`.

## Configuration

- `portainer_version`
    - Default: `latest`
    - Sets the version of Portainer to deploy. For available versions, check docker hub [here](https://hub.docker.com/r/portainer/portainer-ce/tags).
- `portainer_network`
    - Default: `apps`
    - Sets the docker network the container will be attached to.
- `portainer_user`
    - Default: `admin`
    - Name of the admin user. The playbook does not support changing the username.
- `portainer_password`
    - Default: `P@ssw0rd!@#$`
    - Password for the admin user. The playbook does not support changing the password.
- `portainer_agents`
    - Default: `{}`
    - A map containing the name of the portainer-agent as the key, and the host as the value.
    - Example: 
        ```
        portainer_agents:
            example: example.domain.com
            example2: 192.168.1.15
        ```
