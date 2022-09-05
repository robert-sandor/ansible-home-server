# Focalboard

[Focalboard](https://www.focalboard.com/) is an open source, multilingual, self-hosted project management tool that's an alternative to Trello, Notion, and Asana.

Once deployed, Focalboard will be available at `http://<host>:8000`, and if [Traefik](../traefik/README.md) is deployed, on `https://focalboard.<domain>`.

## Configuration

- `focalboard_version`
    - Default: `latest`
    - Version of the Focalboard container to deploy. Available version can be found on [DockerHub](https://hub.docker.com/r/mattermost/focalboard/tags).
- `focalboard_network`
    - Default: `apps`
    - Docker network to add Focalboard to.
- `focalboard_postgres_version`
    - Default: `latest`
    - Version of PostgreSQL to use as a DB for Focalboard. Available version can be found on [DockerHub](https://hub.docker.com/_/postgres/tags).
- `focalboard_postgres_password`
    - Default: `focalboard`
    - Password of the `focalboard` user in the PostgreSQL database, that Focalboard will use for the connection.
- `focalboard_telemetry`
    - Default: `false`
    - Whether to enable telemetry for Focalboard.
