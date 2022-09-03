# Traefik

[Traefik](https://traefik.io/) is used as a reverse proxy for the applications and certificate manager. 
It will create routers and services for each additional service added, based on the labels that are set on each docker container.

Once deployed, Traefik will:
- Listen on port `80` for incoming HTTP requests to route.
- Listen on port `443` for incoming HTTPS requests to route, unless 

## Configuration 

- `traefik_version`
    - Default: `latest`
    - Version of the traefik container to deploy. For available versions check docker hub [here](https://hub.docker.com/_/traefik/tags). 
- `traefik_network`
    - Default: `apps`
    - Docker network that the container will be added to. The apps traefik routes to should be on the same network.
- `traefik_https`
    - Default: `true`
    - Toggles whether Traefik binds to port `443` and handles HTTPS requests.
- `traefik_access_logs`
    - Default: `false`
    - Toggles whether Traefik writes access logs. Useful for debugging an application that is not behaving as expected.
- `traefik_metrics`
    - Default: `false`
    - Toggles whether to enable the [Prometheus](../prometheus/README.md) metrics endpoint for Traefik. For more information, check the [docs](https://doc.traefik.io/traefik/observability/metrics/overview/).
- `traefik_acme_enabled`
    - Default: `false`
    - Toggle to enable automatic certificate management using [Let's Encrypt](https://letsencrypt.org/) protocol. This is only applied if `traefik_https` is enabled.
- `traefik_acme_staging: true`
    - Default: `true`
    - Toggle to use the Staging or Production ACME servers. For testing, use `true`, for production use, change to `false`.
- `traefik_acme_email`
    - Default: `admin@<domain>`
    - Email address that is used to register with [Let's Encrypt](https://letsencrypt.org/). Note that Let's Encrypt will send notifications for certificate expiry to this address.
- `traefik_acme_provider`
    - Default: `cloudflare`
    - The provider to use for the DNS-01 challenge. For other supported providers, check the [Traefik docs](https://doc.traefik.io/traefik/https/acme/#providers).
- `traefik_acme_env`
    - Default:
    ```
    CF_API_EMAIL: email@example.com
    CF_DNS_API_TOKEN: <cloudflare_token>
    ```
    - A map containing environment variables that are required to configure the chosen `traefik_acme_provider`. 
    For necessary values, check the [Traefik docs](https://doc.traefik.io/traefik/https/acme/#providers).
