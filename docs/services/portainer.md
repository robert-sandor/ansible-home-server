# Portainer

[Portainer](https://www.portainer.io/?hsLang=en) is a docker management tool, that can be used to have access to all deployed services, logs, etc. It can be used to managed Docker Swarn or Kubernetes deployments as well. The version used in this project, is the free for personal use CE version.

## Configuration

| Variable | Example/Allowd values | Description |
|----------|-----------------------|-------------|
| `portainer_version` | `latest` | Version of portainer to install. Available version can be found [here](https://hub.docker.com/r/portainer/portainer-ce/tags)
| `portainer_network` | `core` | The network portainer should connect to. If access through [Traefik](traefik.md) is desired, the network should be the same as Traefik's |
| `portainer_autoupdate` | `enable`/`disable`/`monitor` | Whether to auto update or monitor updates for Portainer, if [watchtower](watchtower.md) is installed |
| `portainer_user` | `admin` | The user name of the admin user to configure. |
| `portainer_password` | `p@ssw0rd` | The password to set for the admin user. |
| `portainer_enable_dark_mode` | `yes`/`no` | Whether to enable dark mode for the admin user. |
| `portainer_agents` | `name: example`<br>`host: example.domain.local` | List of portainer agents to add to the instance of Portainer. Every agent has to have a unique name. |
