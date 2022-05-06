# Adguard Home

[Adguard Home](https://adguard.com/en/adguard-home/overview.html) is a network-wide adblocker that acts as a DNS proxy and cache. 

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| adguard_user | yes | `admin` | Username for the account to access Adguard Home |
| adguard_pass | yes | `p@ssw0rd` | Password for the account to access Adguard Home |
| adguard_version | no | `latest` | Adguard Home version - available version can be found [here](https://hub.docker.com/r/adguard/adguardhome/tags). Defaults to `latest` |
| adguard_network | no | `core` | Network that Adguard Home will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| adguard_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Adguard Home, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| adguard_ratelimit | no | `20` | The amount of requests per second a client is allowed to make until they're rate limited. Defaults to `50` |
| adguard_cache_size_mb | no | `4` | Cache size in MiB. This number will be converted to bytes by multiplying with `1024 * 1024`. Defaults to `32` |
| adguard_dns | no | `[ 'https://dns.cloudflare.com/dns-query' ]` | List of upstream DNS servers for Adguard to use. For more info on how these can be configured, see [official documentation](https://github.com/AdguardTeam/AdGuardHome/wiki/Configuration#upstreams) and the list of known [providers](https://kb.adguard.com/en/general/dns-providers). Defaults to Cloudflare's DNS over HTTPS endpoint `https://dns.cloudflare.com/dns-query` and Quad9's DNS over HTTPS endpoint `https://dns.quad9.net/dns-query` |
| adguard_bootstrap | no | `[ '1.1.1.1', '9.9.9.9' ]` | List of DNS servers to use to determine the IP of the upstream DNS servers when they are hostnames. Defaults to `[ '1.1.1.1', '9.9.9.9' ]` (Cloudflare and Quad9 DNS servers) |
| adguard_filters | no | [Filters](#filters) | List of filters to add to Adguard. These will be the lists that block DNS queries. Defaults to the [AdGuard DNS filter](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt) |
| adguard_rewrites | no | [Rewrites](#rewrites) | List of rewrites to add to Adguard. Defaults to empty list. |

## Filters

Filters are lists of domains and addresses that are known for ads, tracking or malware. These DNS requests will be blocked by Adguard.
Adguard supports both filter lists, and allow lists, but this configuration focuses mainly on blocking filters.

To configure a new filter, you need to specify a name for it, and a URL for the file that defines the list. Example

```
adguard_filters:
  - name: 'AdGuard DNS filter'
    url: 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
```

Some well known filters are listed below, but any `/etc/hosts` style filter file could be used here.

- [AdGuard DNS filter](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt)
- [Pihole Gravity](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts)
- [AdAway Default Blocklist](https://adaway.org/hosts.txt)
- [WindowsSpyBlocker](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt)

## Rewrites

DNS rewrites allows to easily configure custom DNS response for a specific domain name.
The configuration is a list of strings, with each string being in the format `<from_domain>|<to_url_or_domain>`, meaning any DNS requests to `from_domain` will be rewritten to the IP or domain found in `to_url_or_domain`.

Some examples:

- `home.domain.com|192.168.1.10` - route all requests to `home.domain.com` to `192.168.1.10` - useful for home network DNS routing
- `*.home.domain.com|192.168.1.10` - route all requests to any subdomain of `home.domain.com` to `192.168.1.10` - useful for home network DNS routing
- `google.com|facebook.com` - adds a CNAME record from `google.com` to `facebook.com`
