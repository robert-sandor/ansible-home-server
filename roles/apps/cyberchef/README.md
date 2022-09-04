# Cyberchef

[Cyberchef](https://github.com/gchq/cyberchef) is a simple, intuitive web app for carrying out all manner of "cyber" operations within a web browser. These operations include simple encoding like XOR and Base64, more complex encryption like AES, DES and Blowfish, creating binary and hexdumps, compression and decompression of data, calculating hashes and checksums, IPv6 and X.509 parsing, changing character encodings, and much more.

## Configuration

- `cyberchef_version`
    - Default: `latest`
    - Version of Cyberchef to deploy. For available versions check [DockerHub](https://hub.docker.com/r/mpepping/cyberchef/tags).
- `cyberchef_network`
    - Default: `apps`
    - Docker network to add Cyberchef to.
