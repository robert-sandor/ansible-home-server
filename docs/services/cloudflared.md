# Cloudflared

WIP docs

## Creating a new tunnel

To create a new tunnel, run the [init.sh](../../services/cloudflared/scripts/init.sh) script on a host with docker installed. This will run a temporary image, allow you to login, and will create a new tunnel with a given name. 

Example usage: `bash init.sh test-tunnel`

*NOTE*: This script should be run from within its folder.
