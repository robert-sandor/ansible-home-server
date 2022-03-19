# qBittorent

[qBittorrent](https://github.com/qbittorrent/qBittorrent) is a bittorrent client, that can integrate well with Sonarr/Radarr for media management. 
This deployment uses the docker image from [linuxserver](https://docs.linuxserver.io/images/docker-qbittorrent).

# Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| `qbt_version` | yes | `latest` | qBittorrent version - available version can be found [on linuxserver's documentation page](https://docs.linuxserver.io/images/docker-qbittorrent) |
| `qbt_network` | no | `latest` | Network that flame will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| `qbt_autoupdate` | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for qBittorrent, if [watchtower](watchtower.md) is installed, defaults to `disable` |
| `qbt_download_volume` | yes | `host-volume` | A docker volume, ideally NFS/SMB, created through [Volume Configuration](../volume_config.md), for where qBittorrent will download the data |
| `qbt_vuetorrent` | no | `yes` / `no` | Whether to download [VueTorrent](https://github.com/WDaan/VueTorrent) as an alternative web UI. | 
| `qbt_config` | yes | Configuration map for qBittorrent | Configurations for qBittorrent. For a complete list of available configurations see the list [here](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-preferences). |
| `qbt_categories` | no | `name: isos`<br>`path: "/downloads/isos"` | List of categories and their download location. For integration with Sonarr and Radarr, it's recommended to have a category for each. |

# Example app configuration


```
web_ui_username: admin
web_ui_password: p@ssw0rd
```
This is to set the username and password for the UI.

```
save_path: "/data/downloads"
```
Defines what the default download folder is for any download on qBittorrent.

```
auto_tmm_enabled: true
```
Whether to enable Automatic Torrent Management, e.g. downloads to the folder defined in categories.

```
max_active_downloads: 50
max_active_torrents: 50
max_active_uploads: 50
```
Max active downloads/torrents/uploads defines how many of each qBittorrent can have active at a time. These values depend on your usage and resources.

```
alt_dl_limit: 5242880
alt_up_limit: 5242880
scheduler_enabled: true
schedule_from_hour: 9
schedule_to_hour: 23
```
Alternate download speed and scheduling. This is useful for scheduling times when qBittorrent won't saturate the download/upload speeds.
In the example, qBittorrent is limited to 5 MB/s download and upload, from 9AM to 11PM every day.
