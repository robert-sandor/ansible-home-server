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

The playbook supports setting any Transmission configuration supported by the Transmission RPC API.
All fields of `transmission_config` will be used to set the appropiate config in Transmission.
For a full, up-to-date reference, you can visit the official documentation [here](https://trac.transmissionbt.com/browser/trunk/extras/rpc-spec.txt#L446)

The list of default configurations applied by the playbook is:
- `alt-speed-down: 15000`
    - Sets alternative download speed to 15 MB/s.
- `alt-speed-up: 15000`
    - Sets alternative upload speed to 15 MB/s.
- `alt-speed-time-begin: 540`
    - Sets the alternative speed schedule to start at 9:00 AM.
- `alt-speed-time-end: 0`
    - Sets the alternative speed schedule to end at 12:00 AM.
- `alt-speed-time-enabled: true`
    - Enables the alternative speed schedule.
- `download-dir: /downloads`
    - Sets the download directory in the container to `/downloads`. This is where the storage method chosen in `transmission_storage` is mounted.
- `download-queue-size: 100`
    - Sets maximum torrent downloads to 100.
- `seed-queue-size: 100`
    - Sets maximum torrent uploads to 100.
- `peer-limit-global: 2000`
    - Sets the peer limit globally to 2000.
- `peer-limit-per-torrent: 20`
    - Sets the peer limit per torrent to 20.
- `rename-partial-files: true`
    - Add `.part` by default to files that are in progress
- `seedRatioLimit: 10`
    - Add a seed ratio limit of 10.
- `seedRatioLimited: true`
    - Enables the seed ratio limit. Once the limit is hit, the torrent will be stopped, but not deleted.
- `idle-seeding-limit: 1440`
    - Add a seed idle time of 1 week for torrents.
- `idle-seeding-limit-enabled: true`
    - Enables the seed idle time. Once the limit is hit, the torrent will be stopped, but not deleted.
- `start-added-torrents: true`
    - Set to automaticalle download added torrents.
