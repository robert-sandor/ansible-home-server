# Registry

[Docker Registry](https://docs.docker.com/registry/) is a stateless, highly scalable server side application that stores and lets you distribute Docker images.
The registry can be configured standalone, or as a pull-through cache for a remote registry server.
The defaults set it as a pull-through cache for the DockerHub registry.

Once deployed, the registry will be available at `http://<domain>:5000`, and if [Traefik](../traefik/README.md) is present `https://registry.<domain>`.

## Configuration

- `registry_version`
    - Default: `latest`
    - The version of the Docker Registry container to deploy. The available versions can be found on [DockerHub](https://hub.docker.com/_/registry/tags).
- `registry_network`
    - Default: `apps`
    - The Docker network to add the Registry container to.
- `registry_location`
    - Default: `path`
    - Whether to use a path on the host as the mount for the registry data, or an NFS share. Allowed values are `path` and `nfs`.
- `registry_path`
    - Default: `{{ project_dir }}/registry/data`
    - The mount path for the registry data, if the `registry_location` is set to `path`.
- `registry_nfs_server`
    - Default: empty
    - The IP or host of the NFS server, when the `registry_location` is set to `nfs`.
- `registry_nfs_path`
    - Default: empty
    - The path on the NFS server to use, when the `registry_location` is set to `nfs`.
- `registry_nfs_opts`
    - Default: `noexec,nolock,rw,soft,nfsvers=4`
    - Additional options to use when mounting the NFS share, when the `registry_location` is set to `nfs`.
- `registry_proxy`
    - Default: `true`
    - Whether to use the registry as a pull-through cache for a differrent proxy server, like the main DocherHub one `https://registry-1.docker.io`.
- `registry_proxy_url`
    - Default: `https://registry-1.docker.io`
    - The URL of the registry to use as a remote proxy for the pull-through cache.
- `registry_proxy_user`
    - Default: empty
    - The user to use to authenticate to the remote proxy registry, if needed.
- `registry_proxy_password`
    - Default: empty
    - The password of the user above, that will be used to authenticate with the remote proxy registry.

## Docker configuration

In order to use the registry as a pull-through cache, it has to be added to the configuration of the Docker daemon as documented [here](https://docs.docker.com/registry/recipes/mirror/):
```
{
  "registry-mirrors": ["https://registry.<domain>"] OR ["http://<domain>:5000"]
}
```

If the registry is not configured with a certificate, you must also add it as an insecure registry in the Docker daemon configuration:
```
{
  "insecure-registries": ["https://registry.<domain>"] OR ["http://<domain>:5000"]
}
```
