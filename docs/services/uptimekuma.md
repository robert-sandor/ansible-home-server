# Uptime Kuma

[Uptime Kuma](https://github.com/louislam/uptime-kuma) is a service monitoring tool, similar to Uptime Robot. This can be used to configure monitors for all kinds of scenarios, and notify if servives are down or non-responsive.

# Configuration

| Variable | Example/Allowd values | Description |
|----------|-----------------------|-------------|
| `uptimekuma_version` | `latest` | The version of Uptime Kuma to use. You can see the versions by checking [github](https://github.com/louislam/uptime-kuma/releases) |
| `uptimekuma_network` | `core` | The network name that Uptime Kuma should attach to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| `uptimekuma_autoupdate` | `enable` / `disable` / `monitor` | Whether to auto update or monitor only |

# App configuration

As of right now, Uptime Kuma does not support a public API that can be used for automation (see issue [here](https://github.com/louislam/uptime-kuma/issues/118)). As of now, all configuration has to be done manually through the UI.
Will try to update the deployment once a public API is enabled for the service.
