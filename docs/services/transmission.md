# Transmission

[Transmission](https://transmissionbt.com/) is a free and open source BitTorrent client. It can integrate with Sonarr/Radarr/etc. for media management. This deployment uses the [linuxserver.io](https://docs.linuxserver.io/images/docker-transmission) image.

# Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| `transmission_version` | yes | `latest` | Transmission version - available version can be found [on linuxserver's documentation page](https://docs.linuxserver.io/images/docker-transmission) |
| `transmission_network` | no | `core-network` | Network that Transmission will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| `transmission_autoupdate` | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Transmission, if [watchtower](watchtower.md) is installed, defaults to `disable` |
| `transmission_download_volume` | yes | `host-volume` | A docker volume, ideally NFS/SMB, created through [Volume Configuration](../volume_config.md), for where Transmission will download the data |
| `transmission_watch_volume` | yes | `watch-volume` | A docker volume, ideally NFS/SMB, created through [Volume Configuration](../volume_config.md), where Tranmission will watch for `.torrent` files |
| `transmission_config` | yes | Configuration map for Transmission | Session configuration for Transmission |

# Volume mappings

The image for Transmission exposes 3 volumes. Here are their internal mapping:
- `/config` - this is where Transmission files are stored - this is mapped to a volume called `transmission-data` by the playbook
- `/downloads` - this is where Transmission expects to download the files - this should ideally be a large NFS/SMB share - the name of this share is given by `transmission_download_volume` config
- `/watch` - this is where Transmission will watch for `.torrent` files - this is optional, but should be mapped to a local volume, whose name is given by `transmission_watch_volume` config - this can also be mapped to a remote NFS/SMB share if the feature is desired

# Session Configuration

Note: For a full, up-to-date reference, you can visit the official documentation [here](https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L446)

| Variable                     | Type       | Description |
|------------------------------|------------|-------------|
| alt-speed-down               | number     | max global download speed (KBps) |
| alt-speed-enabled            | boolean    | true means use the alt speeds |
| alt-speed-time-begin         | number     | when to turn on alt speeds (units: minutes after midnight) |
| alt-speed-time-enabled       | boolean    | true means the scheduled on/off times are used |
| alt-speed-time-end           | number     | when to turn off alt speeds (units: same) |
| alt-speed-time-day           | number     | what day(s) to turn on alt speeds (look at tr_sched_day) |
| alt-speed-up                 | number     | max global upload speed (KBps) |
| blocklist-url                | string     | location of the blocklist to use for "blocklist-update" |
| blocklist-enabled            | boolean    | true means enabled |
| cache-size-mb                | number     | maximum size of the disk cache (MB) |
| download-dir                 | string     | default path to download torrents |
| download-queue-size          | number     | max number of torrents to download at once (see download-queue-enabled) |
| download-queue-enabled       | boolean    | if true, limit how many torrents can be downloaded at once |
| dht-enabled                  | boolean    | true means allow dht in public torrents |
| encryption                   | string     | "required", "preferred", "tolerated" |
| idle-seeding-limit           | number     | torrents we're seeding will be stopped if they're idle for this long |
| idle-seeding-limit-enabled   | boolean    | true if the seeding inactivity limit is honored by default |
| incomplete-dir               | string     | path for incomplete torrents, when enabled |
| incomplete-dir-enabled       | boolean    | true means keep torrents in incomplete-dir until done |
| lpd-enabled                  | boolean    | true means allow Local Peer Discovery in public torrents |
| peer-limit-global            | number     | maximum global number of peers |
| peer-limit-per-torrent       | number     | maximum global number of peers |
| pex-enabled                  | boolean    | true means allow pex in public torrents |
| peer-port                    | number     | port number |
| peer-port-random-on-start    | boolean    | true means pick a random peer port on launch |
| port-forwarding-enabled      | boolean    | true means enabled |
| queue-stalled-enabled        | boolean    | whether or not to consider idle torrents as stalled |
| queue-stalled-minutes        | number     | torrents that are idle for N minuets aren't counted toward seed-queue-size or download-queue-size |
| rename-partial-files         | boolean    | true means append ".part" to incomplete files |
| script-torrent-done-filename | string     | filename of the script to run |
| script-torrent-done-enabled  | boolean    | whether or not to call the "done" script |
| seedRatioLimit               | double     | the default seed ratio for torrents to use |
| seedRatioLimited             | boolean    | true if seedRatioLimit is honored by default |
| seed-queue-size              | number     | max number of torrents to uploaded at once (see seed-queue-enabled) |
| seed-queue-enabled           | boolean    | if true, limit how many torrents can be uploaded at once |
| speed-limit-down             | number     | max global download speed (KBps) |
| speed-limit-down-enabled     | boolean    | true means enabled |
| speed-limit-up               | number     | max global upload speed (KBps) |
| speed-limit-up-enabled       | boolean    | true means enabled |
| start-added-torrents         | boolean    | true means added torrents will be started right away |
| trash-original-torrent-files | boolean    | true means the .torrent file of added torrents will be deleted |
| units                        | object     | see below |
| utp-enabled                  | boolean    | true means allow utp |
