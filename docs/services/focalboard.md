# Focalboard

[Focalboard](https://www.focalboard.com/) is an open source, multilingual, self-hosted project management tool that's an alternative to Trello, Notion, and Asana.
It helps define, organize, track and manage work across individuals and teams. 

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| focalboard_version | no | `latest` | Focalboard version - available version can be found [here](https://hub.docker.com/r/mattermost/focalboard/tags). Defaults to `latest` |
| focalboard_network | no | `core` | Network that focalboard will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| focalboard_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for focalboard, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |

## App configuration

The [Focalboard API](https://github.com/mattermost/focalboard/tree/main/server/swagger) is currently considered Beta, and not final. TBD on when automatic configuration can be implemented, but as of April 2022, it is manual.
