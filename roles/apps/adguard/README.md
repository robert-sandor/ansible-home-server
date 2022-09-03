# Adguard Home

[Adguard Home](https://adguard.com/en/adguard-home/overview.html) is a network-wide adblocker that acts as a DNS proxy and cache. 

## Configuration

---
- `adguard_version`
  - Default: `latest`
  - Version of AdguardHome to deploy. For a list of available versions check [DockerHub](https://hub.docker.com/r/adguard/adguardhome/tags).
- `adguard_network`
  - Default: `apps`
  - Docker network that AdguardHome will be added to.
- `adguard_user`
  - Default: `admin`
  - The username to set for the admin user.
- `adguard_pass`
  - Default: `adguard123`
  - The password for the admin user.
- `adguard_ratelimit`
  - Default: `50`
  - The number of requests per second allowed per client. Setting it to 0 means no limit.
- `adguard_cache_size_mb`
  - Default: `128`
  - AdguardHome cache size in MiB. Increasing this may lead to faster queries, but may use more memory.
- `adguard_dns`
  - Default: 
    ```
    - https://dns.cloudflare.com/dns-query
    - https://dns.quad9.net/dns-query
    ```
  - The upstream DNS servers that AdguardHome will use. The default uses DNS-over-HTTPS servers from Cloudflare and Quad9.
- `adguard_bootstrap`
  - Default:
    ```
    - '1.1.1.1'
    - '9.9.9.9'
    ```
  - DNS servers to use to determine the IP addresses of the upstream DNS servers, if DNS-over-HTTPS or similar is used. The default is set to Cloudflare's DNS `1.1.1.1` and Quad9's DNS `9.9.9.9`
- `adguard_filters`
  - Default:
    ```
    - name: 'AdGuard DNS filter'
      url: 'https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt'
    ```
  - List of DNS filter lists that AdguardHome will use for blocking domains. Each entry needs a `name` and a `url` that points to a file containing the filter list.
  - Some examples of good filter lists:
    - [AdGuard DNS filter](https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt)
    - [Pihole Gravity](https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts)
    - [AdAway Default Blocklist](https://adaway.org/hosts.txt)
    - [WindowsSpyBlocker](https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt)
- `adguard_rewrites`
  - Default: empty
  - Map containing a set of rewrites, where the key is the domain, and the value is the answer AdguardHome will give when queried for the domain.
  - Note: For each entry in this map, 2 entries will be added as rewrites to AdguardHome, to allow all subdomains to be routed to the same host.
    - For example, for an entry `domain.com: 192.168.1.1`, both `domain.com` and `*.domain.com` will be routed to `192.168.1.1`
  - Example:
    ```
    adguard_rewrites:
      gateway.domain.com: 192.168.1.1
      router.domain.com: gateway.domain.com
    ```
