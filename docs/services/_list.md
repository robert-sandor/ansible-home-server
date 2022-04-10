# Services

| Service | Description | Ports | Host |
|---------|-------------|-------|------|
| [Traefik](traefik.md) | Reverse proxy | 80 - http entrypoint<br>443 - https entrypoint<br>8081 - prometheus metrics | `traefik.<domain>` |
| [Flame](flame.md) | Application Dashboard |  5005 - UI | `<domain>` |
| [Watchtower](watchtower.md) | Container update & monitoring | no ports | none |
| [Portainer](portainer.md) | Docker management tool | 9000 - UI | `portainer.<domain>` |
| [Portainer Agent](portainer-agent.md) | Remote agent for Portainer | 9001 - Portainer access | none |
| [Uptime Kuma](uptimekuma.md) | Service health monitoring | 3001 - UI & Webhooks | `uptimekuma.<domain>` |
| [Cloudflared](cloudflared.md) | Cloudflared tunnel | - | - |
| [Wireguard](wireguard.md) | Wireguard VPN | 51820 - UDP tunnel | - |
| [Adguard](adguard.md) | Network-wide Ad blocker | 53 - DNS<br>3000 - UI | `adguard.<domain>` |
| [Pihole](pihole.md) | Network-wide Ad blocker | 53 - DNS<br>8053 - UI | `pihole.<domain>` |
| [dnsmasq](dnsmasq.md) | DNS server | 53 - DNS | - |
| [Qbittorrent](qbittorrent.md) | BitTorrent client | 8082 - UI<br>6881 - P2P port | `qbt.<domain>` |
| [Transmission](transmission.md) | BitTorrent client | 9091 - UI<br>51413 - P2P port | `transmission.<domain>` |
| [Jackett](jackett.md) | Proxy server that translates Queries from Sonarr/Radarr to tracker-site-specific queries | 9117 - UI and API | `jackett.<domain>` |
| [Sonarr](sonarr.md) | Media manager for TV Series | 8989 - UI and API | `sonarr.<domain>` |
| [Radarr](radarr.md) | Media manager for Movies | 7878 - UI and API | `radarr.<domain>` |
| [Plex](plex.md) | Media Server | 32400 - UI | `plex.<domain>` |
| [Overseerr](overseerr.md) | Request management and media discovery tool | 5055 - UI | `overseerr.<domain>` |
| [Mealie](mealie.md) | Recipe and meal planning | 8080 - UI | `mealie.<domain>` |
| [Focalboard](focalboard.md) | OSS alternative to Trello and similar | 8000 - UI | `focalboard.<domain>` |
| [Navidrome](navidrome.md) | Music server, similar to Spotify | 4533 - UI | `navidrome.<domain>` |
| [Cyberchef](cyberchef.md) | String manipulation tool | 8001 - UI | `cyberchef.<domain>`
