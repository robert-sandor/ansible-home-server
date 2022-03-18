# Portainer agent

This agent allows an existing deployment of Portainer to work with the docker environment where this agent is deployed. For a single instance deployment, the agent is not needed.

## Configuration

| Variable | Example/Allowd values | Description |
|----------|-----------------------|-------------|
| `portainer_agent_version` | `latest` | Version of portainer agent to install. Available version can be found [here](https://hub.docker.com/r/portainer/agent/tags)
| `portainer_agent_network` | `core` | The network portainer agent should connect to. This network should have bridge or host access so a [Portainer](portainer.md) instance can connect to the agent |
| `portainer_agent_autoupdate` | `enable`/`disable`/`monitor` | Whether to auto update or monitor updates for Portainer Agent, if [watchtower](watchtower.md) is installed |
