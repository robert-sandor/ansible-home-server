# Services

| Service | Description | Ports | Host |
|---------|-------------|-------|------|
| [Traefik](traefik.md) | Reverse proxy | 80 - http entrypoint<br>443 - https entrypoint<br>8081 - prometheus metrics | `traefik.<domain>` |
| [Watchtower](watchtower.md) | Container update monitoring | no ports | none |
| [Portainer](portainer.md) | Docker management | 9000 - UI | `portainer.<domain>` |
| [Portainer Agent](portainer-agent.md) | Remote agent for Portainer | 9001 - Portainer access | none |
| [Flame](flame.md) | Application Dashboard |  5005 - UI | `<domain>` |
| [Qbittorrent](qbittorrent.md) | Torrent download manager | 8082 - UI<br>6881 - P2P port | `qbt.<domain>` |
