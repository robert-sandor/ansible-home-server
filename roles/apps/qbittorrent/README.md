# qBittorrent

[qBittorrent](https://www.qbittorrent.org/) is a free and open source BitTorrent client. It can integrate with Sonarr/Radarr/etc. for media management. This deployment uses the [linuxserver.io](https://docs.linuxserver.io/images/docker-qbittorrent) image.

Once deployed, Qbittorrent will be available at `http://<host>:8082`, or if [Traefik](../traefik/README.md) is also deployed, on `https://qbittorrent.<domain>`.

## Configuration

- `qbit_version`
    - Default: `latest`
    - Version of the qBittorrent container to deploy. Available versions can be found on [LSIO's Github releases](https://github.com/linuxserver/docker-qbittorrent/releases)
- `qbit_network`
    - Default: `apps`
    - The docker network to add qBittorrent to.
- `qbit_user`
    - Default: `admin`
    - The username to set for qBittorrent authentication. Empty means no authentication.
- `qbit_password`
    - Default: `adminadmin`
    - The password to set for qBittorrent authentication. Empty means no authentication.
- `qbit_storage`
    - Default: `path`
    - Whether to use a path on the host, or an NFS share for downloads and watch directories. Options are `path` and `nfs`.
- `qbit_download_path`
    - Default: `"{{ project_dir }}/qbittorrent"`
    - Path on the host where qBittorrent will download torrents, if `qbit_storage` is set to `path`.
- `qbit_nfs_server`
    - Default: empty
    - The hostname or IP address of the NFS server, if `qbit_storage` is set to `nfs`.
- `qbit_nfs_download`
    - Default: empty
    - The path on the NFS server that qBittorrent should download to, if `qbit_storage` is set to `nfs`.
- `qbit_nfs_opts`
    - Default: `noexec,nolock,rw,soft,nfsvers=4`
    - Additional parameters to set for the NFS mount.
- `qbit_install_vuetorrent`
    - Default: `true`
    - Whether to install and enable [Vuetorrent](https://github.com/WDaan/VueTorrent).
- `qbit_categories`
    - Default: empty
    - A map of categories to setup in qBittorrent, where the key is the category name, and the value is the relative path from `/downloads/`. e.g. `movies: movies` will create a category named `movies` and set the download path for it to `/downloads/movies` in the container. Note that `/downloads/` maps to the storage type chosen by `qbit_storage`.
- `qbit_config`
    - Default: empty
    - A map containing qBittorrent configurations. See [below](#additional-configuration-options) for usage.

## Additional configuration options

The playbook supports setting any qBittorrent configuration that the API supports.
All fields of `qbit_config` will be used to set the appropiate config in qBittorrent.

Example to set automatic torrent management to true:
```
qbit_config:
    auto_tmm_enabled: true
```

For a complete list of configs that qBittorrent supports, check their [API Documentation](https://github.com/qbittorrent/qBittorrent/wiki/WebUI-API-(qBittorrent-4.1)#get-application-preferences).

The list of defaults configs applied by the playbook is:
- `auto_tmm_enabled: true`
    - Sets automatic torrent management to true. This allows the user or client to specify the category only, and the download path will be automatically determined.
- `max_active_torrents: 100`
    - Set max number of active torrents.
- `max_active_downloads: 100`
    - Set max number of active torrents that can be downloading.
- `max_active_uploads: 100`
    - Set max number of active torrents that can be seeding.
- `scheduler_enabled: true`
    - Enable scheduled alternate speeds. This is useful to prevent the client saturating the network during work hours, for example. By default the schedule is set from 9:00 AM to 12:00 AM.
- `schedule_from_hour: 9`
    - Sets the scheduled start hour.
- `schedule_from_min: 0`
    - Sets the scheduled start minute.
- `schedule_to_hour: 0`
    - Sets the scheduled end hour.
- `schedule_to_min: 0`
    - Sets the scheduled end minute.
- `alt_dl_limit: 15360`
    - Sets the alternate download limit, in KiB/s. Default is 15 MiB/s.
- `alt_up_limit: 15360`
    - Sets the alternate upload limit, in KiB/s. Default is 15 MiB/s.
- `max_connec: 2000`
    - Sets global maximum connections to 2000.
- `max_connec_per_torrent: 20`
    - Sets maximum connections per torrent to 20.
