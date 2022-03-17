# Host Variables

Files here define variables for each host. The files in this folder should be in YML format, and have the file name as `<host_name>.yml`. Note that here, the `host_name` refers to the name of the host in the Ansible inventory file, and not to the actual hostname.

For a full list of variables, check [host variables](../docs/host_vars.md).

Variables that make most sense as host-specific variables are:
- `domain`
- `networks`
- `volumes`