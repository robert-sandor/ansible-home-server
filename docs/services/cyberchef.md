# Cyberchef

[Cyberchef](https://github.com/gchq/cyberchef) is a simple, intuitive web app for carrying out all manner of "cyber" operations within a web browser. These operations include simple encoding like XOR and Base64, more complex encryption like AES, DES and Blowfish, creating binary and hexdumps, compression and decompression of data, calculating hashes and checksums, IPv6 and X.509 parsing, changing character encodings, and much more.

## Configuration

| Variable | Required | Example | Description |
|----------|----------|---------|-------------|
| cyberchef_version | no | `latest` | cyberchef version - available version can be found [here](https://hub.docker.com/r/mpepping/cyberchef/tags). Defaults to `latest` |
| cyberchef_network | no | `core` | Network that cyberchef will attach itself to. For access from [Traefik](traefik.md) it should share the same network. This defaults to the first network defined in the [host config](../host_vars.md) |
| cyberchef_autoupdate | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for cyberchef, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
