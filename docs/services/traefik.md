# Traefik

Traefik is used as an application proxy, router and certificate manager. It will create routers and services for each additional service added, based on the labels that are set on each docker container.

## Configuration 

| Variable | Required | Example/Allowd values | Description |
|----------|----------|-----------------------|-------------|
| `traefik_version` | no | `latest`, `v2.6` | The version of traefik to use. You can see the versions by checking [docker hub](https://hub.docker.com/_/traefik?tab=tags). Defaults to `latest` |
| `traefik_network` | no | `traefik`, `common` | The network name that traefik should attach to. This defaults to the first network defined in the [host config](../host_vars.md) |
| `traefik_https` | no | `true` / `false` | Whether to use HTTPS with traefik. If this is on, Traefik will bind to port 443, and will route HTTP requests to HTTPS automatically. It's recommended to have ACME turned on as well |
| `traefik_access_logs` | no | `true` / `false` | Whether to enable Traefik [access logs](https://doc.traefik.io/traefik/observability/access-logs/). Defaults to `false` |
| `traefik_metrics` | no | `true` / `false` | Whether to enable Traefik [metrics with prometheus](https://doc.traefik.io/traefik/observability/metrics/prometheus/). Defaults to `false` |
| `traefik_autoupdate` | no | `enable` / `disable` / `monitor` | Whether to auto update or monitor updates for Traefik, if [watchtower](watchtower.md) is installed. Defaults to `monitor` |
| `traefik_acme` | no | `true` / `false` | Whether to enable Let's Encrypt certificate using [ACME](https://doc.traefik.io/traefik/https/acme/)<br>Note: This implements DNS01 challenge as of right now. Read mode about it [here](https://doc.traefik.io/traefik/https/acme/#dnschallenge). Defaults to `false` |
| `traefik_acme_staging` | no | `true` / `false` | Whether to use the staging server for Let's Encrypt instead of the production one. Use this when testing the deployment. Defaults to `false` |
| `traefik_acme_email` | only if `traefik_acme` is `true` | `change.me@email.com` | The email address to use when registering the certificate through Let's Encrypt. You will receive notifications when the certificates expire. Traefik will re-issue the certificates automatically, so no manual action is required |
| `traefik_acme_provider` | only if `traefik_acme` is `true` | `cloudflare` | What provider to use for the DNS01 challenge. List of all providers, and their configuration is [here](https://doc.traefik.io/traefik/https/acme/#providers) |
| `traefik_acme_env` | no | Map of env values to configure the provider<br>example for cloudflare:<br>`CF_API_EMAIL: changeme@email.com`<br>`CF_DNS_API_TOKEN: cf_token` | Configuration for the provider chosen above. The values you need to set are part of the provider list [here](https://doc.traefik.io/traefik/https/acme/#providers) |
