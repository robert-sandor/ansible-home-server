# Aria2

Aria2 is a lightweight multi-protocol & multi-source command-line download utility. AriaNG is used as a web frontend for aria2.

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| aria2_download_path | yes | `/home/user/downloads` | Path to where aria2 will download the files. This should ideally be an NFS/SMB mounted path. |
| aria2_version | no | `latest` | Aria2 version - available version can be found [here](https://hub.docker.com/r/p3terx/aria2-pro/tags). Defaults to `latest` |
| ariang_version | no | `latest` | AriaNG version - available version can be found [here](https://hub.docker.com/r/p3terx/ariang/tags). Defaults to `latest` |
| aria2_network | no | `core` | Network that Aria2 and AriaNG will attach themselves to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| aria2_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Adguard Home, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| ariang_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Adguard Home, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |

## Manual configuration

