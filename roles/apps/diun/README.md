# Watchtower

[Watchtower](https://containrrr.dev/watchtower/) is used to monitor for new docker images for the deployed apps. 
Watchtower will watch each registered container, and will notify using one of the suppoert notification mechanism.

## Configuration

- `watchtower_version`
    - Default: `latest`
    - Watchtower version to deploy. For available versions check [DockerHub](https://hub.docker.com/r/containrrr/watchtower/tags).
- `watchtower_network`
    - Default: `apps`
    - Docker network to add watchtower to.
- `watchtower_schedule`
    - Default: `0 0 0 * * *`
    - Cron schedule for when watchtower will check for new docker images. Check [crontab guru](https://crontab.guru/) for setting this up if you're not familiar with cron expressions.
- `watchtower_notifications`
    - Default: `none`
    - Which notification system watchtower should use. This playbook supports `slack`, `discord` and `gotify` as options.
- `watchtower_discord_hook`
    - Default: empty
    - A Discord webhook to send the notifications to. To get this value, check documentation [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
- `watchtower_slack_hook`
    - Default: empty
    - A Slack webhook to send the notifications to. To get this value, check documentation [here](https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack)
- `watchtower_gotify_url`
    - Default: `http://gotify:80`
    - The URL for a Gotify server to use for notifications.
- `watchtower_gotify_token`
    - Default: empty
    - The Gotify API token to use when sending notifications to Gotify. For more information check [Gotify Docs](https://gotify.net/docs/pushmsg).
