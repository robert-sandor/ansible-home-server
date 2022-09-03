# TEMPLATE

[PyLoad]() is a simple file downloader.

Once deployed, PyLoad will be available on port `8010`, or if using [Traefik](../traefik/README.md) at `pyload.<domain>`.

## Configuration

- `pyload_version: latest`
    - Default: ``
    - PyLoad container version to deploy. For available versions check LSIO releases [here]().
- `pyload_network`
    - Default: `apps`
    - Docker network PyLoad will be added to.
- `pyload_download_location`
    - Default: `path`
    - Download location to set for PyLoad. This can be a `path`, or an `nfs` mount.
    - A value set as `path` will mount a directory from the host into the container, whereas `nfs` will create an NFSv4 mount using a docker volume.
- `pyload_download_path`
    - Default: `{{ project_dir }}/pyload`
    - The directory to set as the download path for PyLoad, if `pyload_download_location`is set to `path`.
- `pyload_nfs_server`
    - Default: empty
    - IP address or hostname for the NFS server to connect to, if `pyload_download_location`is set to `nfs`.
- `pyload_nfs_path`
    - Default: empty
    - Path to mount from the NFS server, if `pyload_download_location`is set to `nfs`.
- `pyload_nfs_opts`
    - Default: `noexec,nolock,rw,soft,nfsvers=4`
    - Additional options to add to the NFS connection.
