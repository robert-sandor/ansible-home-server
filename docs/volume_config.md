# Volumes

Here's a list of variables that can be set for each docker volume. 

## Local

For `local` docker volumes, only the `name` and `type` are required.

```
volumes:
  - name: data
    type: local
```

## NFS

For `nfs` and `nfs4` docker volumes, `host` and `device` are also required. Also, make sure the host's user has the needed (read-only, or read-write) access to the share, and the host is allowed to connect.

```
volumes:
  - name: nfs-share
    type: nfs
    host: 192.168.1./ NFS42
    device: media
```

## CIFS / SMB

For **cifs**/**smb** docker volumes, you need to declare the `user` and `password` variables as well. Also, make sure the user has the correct (read-only or read-write) access to the share.

```
volumes:
  - name: cifs-share
    type: cifs
    host: 192.168.1.2
    device: media
    user: media
    password: p@ssw0rd
```

| Variable | Required | Allowed / Example Values | Description |
|----------|----------|--------------------------|-------------|
| name | yes | media, backups | The name of the docker volume
| type | yes | local / nfs / nfs4 / cifs / smb | The type of the volume:<br>**local**: just a simple local docker volume that can be shared by multiple services<br>**nfs**/**nfs4**: connect to an NFS (Linux/Unix) share. **nfs4** just denotes version 4 of NFS<br>**cifs**/**smb**: connect to a CIFS/SMB (Windows) share |
| host | no | 192.168.1.5, nas.domain.local | the hostname or IP address where the file server is reachable by the host - note: this is required for NFS and CIFS/SMB |
| device | no | media, backup | The NFS or CIFS/SMB share/device name - consult your file server for the correct name |
| user | no | media | The username to use when connecting to CIFS/SMB. |
| password | no | p@ssw0rd | The password of the user used to connect to CIFS/SMB.
| options | no | "file_mode=0775,dir_mode=0775,rw" | Additional options to pass to the mount command. **Only change this is you know what you are doing.** |
 