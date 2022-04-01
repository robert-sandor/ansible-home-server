# Portainer

[Portainer](https://www.portainer.io/?hsLang=en) is a docker management tool, that can be used to have access to all deployed services, logs, etc. It can be used to managed Docker Swarn or Kubernetes deployments as well. The version used in this project, is the free for personal use CE version.

## Configuration

| Variable | Required | Example/Allowed values | Description |
|----------|----------|-----------------------|-------------|
| `portainer_version` | no | `latest` | Version of portainer to install. Available version can be found [here](https://hub.docker.com/r/portainer/portainer-ce/tags). Defaults to `latest` |
| `portainer_network` | no | `core` | The network portainer should connect to. If access through [Traefik](traefik.md) is desired, the network should be the same as Traefik's. This defaults to the first network defined in the [host config](../host_vars.md) |
| `portainer_autoupdate` | no | `enable`/`disable`/`monitor` | Whether to auto update or monitor updates for Portainer, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| `portainer_user` | yes | `admin` | The user name of the admin user to configure. |
| `portainer_password` | yes | `p@ssw0rd` | The password to set for the admin user. |
| `portainer_enable_dark_mode` | no | `yes`/`no` | Whether to enable dark mode for the admin user. Defaults to `yes` |
| `portainer_agents` | no | `name: example`<br>`host: example.domain.local` | List of portainer agents to add to the instance of Portainer. Every agent has to have a unique name. |
