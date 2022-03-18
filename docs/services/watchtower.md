# Watchtower

[Watchtower](https://containrrr.dev/watchtower/) is used to monitor and automatically update services. Watchtower will watch each registered container, and will pull the new image, recreating the container if needed.

## Usage

Each service has the a configuration like `<service>-autoupdate` which is the flag for watchtower to update said container. This flag can have one of three values:
- `yes` - watchtower will automatically update this container if a newer image is found
- `no` - watchtower will ignore this container altogether
- `monitor` - watchtower will monitor for new images for this container, and send a notification, but will not modify the container itself

## Notifications

[Notifications](https://containrrr.dev/watchtower/notifications/) are currently only supported for Slack and Discord. The Discord notifications are supported through the Slack notifications, as Discord has support for Slack notifications as well. Support for other notification mechanisms is TBD.

For [Slack](https://containrrr.dev/watchtower/notifications/#slack) you need to providde the Slack hook URL for the channel you want to post in. For Discord, you need to provide the webhook, and append `/slack` at the end. Discord will receive the notifications in Slack's format, and present them in the Discord channel. 

## Configurations

| Variable | Example/Allowd values | Description |
|----------|-----------------------|-------------|
| `watchtower_version` | `latest`, `v1.4.0` | The version of watchtower to use. You can see the versions by checking [github](https://github.com/containrrr/watchtower/releases) |
| `watchtower_network` | `core` | The network name that watchtower should attach to. This should be one of the networks defined in the host vars |
| `watchtower_schedule` | `0 0 1 * * *`<br>(1 AM every day) | The cron schedule for when watchtower should run. This can be any valid cron expression, but it's recommended to run this on a daily or weekly cadence for the best results. |
| `watchtower_discord` | `yes` / `no` | Whether to enable Notifications through Slack/Discord |
| `watchtower_discord_hook` | `https://discord.com/api/webhooks/.../.../slack` | The Slack/Discord webhook to use for notifications |
| `watchtower_autoupdate` | `enable` / `disable` / `monitor` | Whether to auto update or monitor only |
