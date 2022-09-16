# Tailscale

[Tailscale](https://tailscale.com/) is an easy to set up VPN that uses Wireguard.

You'll need an account to use Tailscale, and a free version is available with some restrictions on the number of users, devices, etc.

## Example use case

You can configure Tailscale to connect to the tailnet (tailscale network) and act as a gateway for your home network.
For this, you'll need to add your local network's CIDR to the `tailscale_advertise_routes` variable.
For example, for a usual home network `192.168.0.0/24`, the configuration will look like this:
```
tailscale_advertise_routes:
  - 192.168.0.0/24
```

You can also set the nameservers of the tailnet to your own self-hosted DNS servers, e.g. [AdguardHome](../adguard/README.md). 
This configuration is unfortunately not supported through the API, and it needs to be done manually.
To support the local routing capabilities of a self-hosted DNS server, you should add the nameserver(s) without a search domain, and set them to override the local DNS of the connected devices.

With this setup, once connected to the Tailscale VPN, you can use domain names, and connect to any device on your home network while away.

## Configuration

- `tailscale_api_key`
    - Default: empty
    - A tailscale API key to use to connect to the API. This can be generated from the admin console of Tailscale.
- `tailscale_tailnet`
    - Default: empty
    - The name of the network in Tailscale. This can be identified by the name shown in the admin console, top-right next to the Tailscale logo.
- `tailscale_exit_node`
    - Default: `false`
    - Whether to configure the device as an [exit node](https://tailscale.com/kb/1103/exit-nodes/).
- `tailscale_enable_routes`
    - Default: `true`
    - Whether to automatically enable the advertised routes configured in `tailscale_advertise_routes`. If this is set to `false`, you'll need to manually enable them in the admin console.
- `tailscale_advertise_routes`
    - Default: `[]`
    - A set of CIDRs, that the device will advertise. For more information, check the [subnet router docs](https://tailscale.com/kb/1019/subnets/)
    - Examples: `192.168.0.0/24`, `10.0.0.0/8`
