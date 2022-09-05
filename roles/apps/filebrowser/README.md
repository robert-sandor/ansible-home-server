# Filebrowser

[Filebrowser](https://filebrowser.org) is a create-your-own-cloud-kind of software where you can install it on a server, direct it to a path and then access your files through a nice web interface.

Once deployed, Filebrowser is available at `http://<domain>:8083`, or if [Traefik](../traefik/README.md) is also deployed at `https://filebrowser.<domain>`. The default user is `admin`, and the default password is `admin`.

## Configuration

- `filebrowser_version`
    - Default: `latest`
    - Version of the Filebrowser container to deploy. Available version can be found on [DockerHub](https://hub.docker.com/r/filebrowser/filebrowser/tags).
- `filebrowser_network`
    - Default: `apps`
    - The Docker network to add Filebrowser.
- `filebrowser_location`
    - Default: `path`
    - Whether to use a host path or an NFS share as the path to browse. The allowed values are `path` and `nfs`.
- `filebrowser_path`
    - Default: `"{{ project_dir }}"`
    - The host path to use when the `filebrowser_location` is set to `path`.
- `filebrowser_nfs_server`
    - Default: empty
    - The NFS server to use when the `filebrowser_location` is set to `nfs`.
- `filebrowser_nfs_path`
    - Default: empty
    - The path on the NFS server to use when the `filebrowser_location` is set to `nfs`.
- `filebrowser_nfs_opts`
    - Default: `noexec,nolock,rw,soft,nfsvers=4`
    - Additional options to use when connecting to an NFS server.
