# Wireguard

[Wireguard](https://www.wireguard.com/) is a next generation VPN, that focuses on beng simple fast and secure by default.
This playbook uses the [LinuxServer.io wireguard image](https://docs.linuxserver.io/images/docker-wireguard).

*Note*: This requires the `wireguard` kernel module to be running on the host system. The playbook will attempt to enable this automatically, but if it fails to do so, the server will not start successfully.

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| wg_version | no | `latest` | wireguard image version - available version can be found [here](https://github.com/linuxserver/docker-wireguard/releases). Defaults to `latest` |
| wg_network | no | `core` | Network that wireguard Home will attach itself to. This defaults to the first network defined in the [host config](../host_vars.md) |
| wg_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for wireguard Home, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| wg_server_url | no | `wireguard.domain.com` | External IP or domain name for docker host. Used in server mode. If set to `auto`, the container will try to determine and set the external IP automatically. Defaults to `auto`. |
| wg_server_port | no | `51820` | External port for docker host. Used in server mode. Defaults to `51820` |
| wg_peers | no | `5` or `phone,tablet,laptop` | Number of peers to create confs for. Can also be a list of names: `myPC,myPhone,myTablet` (alphanumeric only). Defaults to `1` (1 unnamed peer) |
| wg_dns | no | `1.1.1.1` | DNS server set in peer/client configs (can be set as `1.1.1.1`). Defaults to `auto`, which uses wireguard docker host's DNS via included CoreDNS forward. |
| wg_subnet | no | `10.13.13.0` | Internal subnet for the wireguard and server and peers (only change if it clashes). Defaults to `10.13.13.0` |
| wg_allowed_ips | no | `0.0.0.0/0` | The IPs/Ranges that the peers will be able to reach using the VPN connection. Defaults to `0.0.0.0/0` which will cause ALL traffic to route through the VPN, if you want split tunneling, set this to only the IPs you would like to use the tunnel AND the ip of the server's WG ip, such as `10.13.13.1`. |

## Additional notes

You can get the QR codes for the peers, by using `docker exec -it wireguard /app/show-peer <peer_name_or_number>` on the host where wireguard container is deployed. These will be shown in the logs as well when the server starts, and can be viewed either from [Portainer](portainer.md) or by using `docker logs -f wireguard`. The configuration files are also avaialble in the config volume, and can be retrieved by using `docker cp wireguard:/config/<peer_folder>/<peer_folder>.conf /path/to/downloads/<peer_folder>.conf` where `peer_folder` will be `peerX` in case of using numbers, or `peer_<name>` in case of using names.

Adding new peers is as simple as increasing the number, or adding a new name to the list. The configurations will be kept for the existing peers, and new ones generated for new peers.
