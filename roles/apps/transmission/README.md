# Transmission

[Transmission](https://transmissionbt.com/) is a free and open source BitTorrent client. It can integrate with Sonarr/Radarr/etc. for media management. This deployment uses the [linuxserver.io](https://docs.linuxserver.io/images/docker-transmission) image.

Once deployed, Transmission will be available at `http://<host>:9001`, or if [Traefik](../traefik/README.md) is also deployed, on `https://transmission.<domain>`.

## Configuration

- `transmission_version`
    - Default: `latest`
    - Version of the Transmission container to deploy. Available versions can be found on [LSIO's Github releases](https://github.com/linuxserver/docker-transmission/releases)
- `transmission_network`
    - Default: `apps`
    - The docker network to add transmission to.
- `transmission_user`
    - Default: empty
    - The username to set for tranmission authentication. Empty means no authentication.
- `transmission_password`
    - Default: empty
    - The password to set for tranmission authentication. Empty means no authentication.
- `transmission_ui`
    - Default: `flood-for-transmission`
    - One of the alternate UI options for Transmission. Options are `combustion-release`, `transmission-web-control`, `kettu`, `flood-for-transmission`, and `transmissionic`.
- `transmission_storage`
    - Default: `path`
    - Whether to use a path on the host, or an NFS share for downloads and watch directories. Options are `path` and `nfs`.
- `transmission_download_path`
    - Default: `"{{ project_dir }}/transmission"`
    - Path on the host where Transmission will download torrents, if `transmission_storage` is set to `path`.
- `transmission_watch_path`
    - Default: `"{{ project_dir }}/transmission"`
    - Path on the host where Transmission will watch for torrent files to download, if `transmission_storage` is set to `path`.
- `transmission_nfs_server`
    - Default: empty
    - The hostname or IP address of the NFS server, if `transmission_storage` is set to `nfs`.
- `transmission_nfs_download`
    - Default: empty
    - The path on the NFS server that Transmission should download to, if `transmission_storage` is set to `nfs`.
- `transmission_nfs_watch`
    - Default: empty
    - The path on the NFS server that Transmission should watch, if `transmission_storage` is set to `nfs`.
- `transmission_nfs_opts`
    - Default: `noexec,nolock,rw,soft,nfsvers=4`
    - Additional parameters to set for the NFS mount.
- `transmission_config`
    - Default: `{}`
    - Configurations for Transmission. Check [below](#transmission-app-configuration).


## Transmission App Configuration

Note: For a full, up-to-date reference, you can visit the official documentation [here](https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L446)

| Variable                     | Type       | Description                                                                                       |
|------------------------------|------------|---------------------------------------------------------------------------------------------------|
| alt-speed-down               | number     | max global download speed (KBps)                                                                  |
| alt-speed-enabled            | boolean    | true means use the alt speeds                                                                     |
| alt-speed-time-begin         | number     | when to turn on alt speeds (units: minutes after midnight)                                        |
| alt-speed-time-enabled       | boolean    | true means the scheduled on/off times are used                                                    |
| alt-speed-time-end           | number     | when to turn off alt speeds (units: same)                                                         |
| alt-speed-time-day           | number     | what day(s) to turn on alt speeds (look at tr_sched_day)                                          |
| alt-speed-up                 | number     | max global upload speed (KBps)                                                                    |
| blocklist-url                | string     | location of the blocklist to use for "blocklist-update"                                           |
| blocklist-enabled            | boolean    | true means enabled                                                                                |
| cache-size-mb                | number     | maximum size of the disk cache (MB)                                                               |
| download-dir                 | string     | default path to download torrents                                                                 |
| download-queue-size          | number     | max number of torrents to download at once (see download-queue-enabled)                           |
| download-queue-enabled       | boolean    | if true, limit how many torrents can be downloaded at once                                        |
| dht-enabled                  | boolean    | true means allow dht in public torrents                                                           |
| encryption                   | string     | "required", "preferred", "tolerated"                                                              |
| idle-seeding-limit           | number     | torrents we're seeding will be stopped if they're idle for this long                              |
| idle-seeding-limit-enabled   | boolean    | true if the seeding inactivity limit is honored by default                                        |
| incomplete-dir               | string     | path for incomplete torrents, when enabled                                                        |
| incomplete-dir-enabled       | boolean    | true means keep torrents in incomplete-dir until done                                             |
| lpd-enabled                  | boolean    | true means allow Local Peer Discovery in public torrents                                          |
| peer-limit-global            | number     | maximum global number of peers                                                                    |
| peer-limit-per-torrent       | number     | maximum global number of peers                                                                    |
| pex-enabled                  | boolean    | true means allow pex in public torrents                                                           |
| peer-port                    | number     | port number                                                                                       |
| peer-port-random-on-start    | boolean    | true means pick a random peer port on launch                                                      |
| port-forwarding-enabled      | boolean    | true means enabled                                                                                |
| queue-stalled-enabled        | boolean    | whether or not to consider idle torrents as stalled                                               |
| queue-stalled-minutes        | number     | torrents that are idle for N minuets aren't counted toward seed-queue-size or download-queue-size |
| rename-partial-files         | boolean    | true means append ".part" to incomplete files                                                     |
| script-torrent-done-filename | string     | filename of the script to run                                                                     |
| script-torrent-done-enabled  | boolean    | whether or not to call the "done" script                                                          |
| seedRatioLimit               | double     | the default seed ratio for torrents to use                                                        |
| seedRatioLimited             | boolean    | true if seedRatioLimit is honored by default                                                      |
| seed-queue-size              | number     | max number of torrents to uploaded at once (see seed-queue-enabled)                               |
| seed-queue-enabled           | boolean    | if true, limit how many torrents can be uploaded at once                                          |
| speed-limit-down             | number     | max global download speed (KBps)                                                                  |
| speed-limit-down-enabled     | boolean    | true means enabled                                                                                |
| speed-limit-up               | number     | max global upload speed (KBps)                                                                    |
| speed-limit-up-enabled       | boolean    | true means enabled                                                                                |
| start-added-torrents         | boolean    | true means added torrents will be started right away                                              |
| trash-original-torrent-files | boolean    | true means the .torrent file of added torrents will be deleted                                    |
| utp-enabled                  | boolean    | true means allow utp                                                                              |
