# Cloudflared

[Cloudflared](https://github.com/cloudflare/cloudflared) is a tunneling daemon that proxies traffic from the Cloudflare network to your origins. This daemon sits between Cloudflare network and your origin (e.g. a webserver).

## Setup

Cloudflared requires logging in using a URL, and that process can not be automated in a reasonable way. Hence, this service requires a bit of manual configuration.
There are two ways to login cloudflared using this playbook:
1. Login pre-emptively, and drop the `cert.pem` file into the `files` directory in the role. If the file is found there when running the playbook, it will be copied over to the server, and login is no longer necessary.
2. Run the playbook to install cloudflared on the server, and connect to the server using SSH and login there directly. This requires running the playbook twice, once to install and once to configure, but can easily be done by using ansible tags (append `-t cloudflared` to run only the cloudflared part of the playbook).

For either option, you'll need to run `cloudflared tunnel login`, which will then present a URL. By going to the URL, and authorizing the login a `cert.pem` file will be created, by default in the `~/.cloudflared` directory.

## Configuration

- `cloudflared_version`
    - Default: `latest`
    - The version of cloudflared to install on the host. Available versions can be found on [Cloudflared's Github repository](https://github.com/cloudflare/cloudflared/releases).
- `cloudflared_tunnel`
    - Default: `"{{ ansible_hostname }}"`
    - The name of the tunnel to create. **NOTE** The name of the tunnel should be unique, and not used by another host, as the instance of cloudflared can not control the tunnel unless it has it's configuration file. If you want to reuse an existing tunnel, you must copy the tunnel's configuration file to the `~/.cloudflared` directory on the server before the tunnel will work.
- `cloudflared_ingress`
    - Default: `{}`
    - This map defines the routing for the tunnel. The keys of the map are the hostnames that will be routed, and the value is the service to route to.
        - Example: to route connections from `gitea.domain.example` to a gitea server running on host `192.168.1.5` and port `3000`, the configuration would be `gitea.domain.example: http://192.168.1.5:3000`
    - This configuration only supports simple routing for now. The other [configuration options](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide/local/local-management/ingress/) might be added at a later date.
