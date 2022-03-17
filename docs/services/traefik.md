# Traefik

Traefik is used as an application proxy, router and certificate manager. It will create routers and services for each additional service added, based on the labels that are set on each docker container.

Traefik variables:

| Variable | Example/Allowd values | Description |
|----------|-----------------------|-------------|
| `traefik_version` | `latest`, `v2.6` | The version of traefik to use. You can see the versions by checkink [docker hub](https://hub.docker.com/_/traefik?tab=tags) |
| `traefik_network` | `traefik`, `common` | The network name that traefik should attach to. This should be one of the networks defined in the host vars |
| `traefik_https` | `yes`/`no` | Whether to use HTTPS with traefik. If this is on, Traefik will bind to port 443, and will route HTTP requests to HTTPS automatically. It's recommended to have ACME turned on as well |
| `traefik_access_logs` | `yes`/`no` | Whether to enable Traefik [access logs](https://doc.traefik.io/traefik/observability/access-logs/) |
| `traefik_metrics` | `yes`/`no` | Whether to enable Traefik [metrics with prometheus](https://doc.traefik.io/traefik/observability/metrics/prometheus/) |
| `traefik_autoupdate` | `yes`/`no` | Whether to auto update Traefik, if [watchtower](watchtower.md) is installed |
| `traefik_acme` | `yes`/`no` | Whether to enable Let's Encrypt certificate using [ACME](https://doc.traefik.io/traefik/https/acme/)<br>Note: This implements DNS01 challenge as of right now. Read mode about it [here](https://doc.traefik.io/traefik/https/acme/#dnschallenge) |
| `traefik_acme_staging` | `yes`/`no` | Whether to use the staging server for Let's Encrypt instead of the production one. Use this when testing the deployment. |
| `traefik_acme_email` | `change.me@email.com` | The email address to use when registering the certificate through Let's Encrypt. You will receive notifications when the certificates expire. Traefik will re-issue the certificates automatically, so no manual action is required |
| `traefik_acme_provider` | `cloudflare` | What provider to use for the DNS01 challenge. List of all providers, and their configuration is [here](https://doc.traefik.io/traefik/https/acme/#providers) |
| `traefik_acme_env` | Map of env values to configure the provider<br>example for cloudflare:<br>`CF_API_EMAIL: changeme@email.com`<br>`CF_DNS_API_TOKEN: cf_token` | Configuration for the provider chosen above. The values you need to set are part of the provider list [here](https://doc.traefik.io/traefik/https/acme/#providers) |