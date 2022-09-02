# Host variables

Here's a comprehensive list of all host-level variables, their usage and example/allowed values

| Variable | Allowed / Example Values | Description |
|----------|--------------------------|-------------|
| timezone | Etc/UTC, Europe/London, America/New_York | Sets the Unix timezone for the host on install |
| project_dir | `/home/user/homeserver`, `/opt/homeserver` | Path to a directory where compose files and other configuration files will be kept on the host |
| domain | example.com, server.local | Sets the domain for the host, all services deployed here will be routed based on the service name and the domain, e.g. `plex.<domain>` |
| packages | `- git`<br>`- cifs-utils` | Defined a list of packages to install on the host |
| networks | `- traefik`<br>`- media` | Defines the docker networks that will be created on the host |
| volumes | list of [volume configurations](volume_config.md) | Defines the docker volumes to create on the host. This is most useful to connect NFS/SMB shares to the docker services. For more info, check [volume configurations](volume_config.md) |
| services | list of [services](services/_list.md) | Defines the services to install on the host. For more    information on the services, check the documentation for each service. |




