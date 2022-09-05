# Gitea

[Gitea](https://gitea.io/en-us/) is a community managed lightweight code hosting solution written in Go. It is published under the MIT license.

Once deployed, Gitea will be available at `http://<host>:3030`, or if [Traefik](../traefik/README.md) is also deployed on the host, on `https://gitea.<domain>`.

## Configuration

- `gitea_version`
    - Default: `latest`
    - Gitea version to deploy. Available versions can be found on [DockerHub](https://hub.docker.com/r/gitea/gitea/tags).
- `gitea_network`
    - Default: `apps`
    - Docker network to add Gitea to.
- `gitea_http_port`
    - Default: `3030`
    - The port to use for HTTP connections to Gitea.
- `gitea_ssh_port`
    - Default: `2222`
    - The port to use for SSH connections to Gitea.
- `gitea_postgres_version`
    - Default: `14`
    - The version of PostgreSQL to use as the DB for Gitea. Available versions can be found on [DockerHub](https://hub.docker.com/_/postgres/tags).
- `gitea_postgres_user`
    - Default: `gitea`
    - The username for the PostgreSQL user that Gitea will use for the connection to the DB.
- `gitea_postgres_password`
    - Default: `gitea`
    - The password for the PostgreSQL user that Gitea will use for the connection to the DB.
- `gitea_app_name`
    - Default: `Gitea`
    - The name to display on the application for Gitea.
- `gitea_default_theme`
    - Default: `arc-green`
    - The default theme to use for the application.
- `gitea_admin_user`
    - Default: `gitea`
    - The username for the Gitea admin user.
- `gitea_admin_password`
    - Default: `gitea`
    - The password for the Gitea admin user.
- `gitea_admin_email`
    - Default: `admin@{{ domain }}`
    - The email address for the Gitea admin user.
- `gitea_smtp_host`
    - Default: `""`
    - An SMTP host, if using email notifications.
- `gitea_smtp_from`
    - Default: `""`
    - Who is the sender of the emails if using notifications.
- `gitea_smtp_user`
    - Default: `""`
    - Username to connect to the SMTP server.
- `gitea_smtp_passwd`
    - Default: `""`
    - Password to connect to the SMTP server.
- `gitea_enable_federated_avatar`
    - Default: `true`
    - Whether to enable Federated Avatars.
- `gitea_enable_open_id_sign_in`
    - Default: `true`
    - Whether to enable OpenID sign in.
- `gitea_enable_open_id_sign_up`
    - Default: `true`
    - Whether to enable OpenID sign up.
- `gitea_default_allow_create_organization`
    - Default: `true`
    - Whether to allow creating organizations by default.
- `gitea_default_enable_timetracking`
    - Default: `true`
    - Whether to enable the timetracking feature.
- `gitea_password_algorithm`
    - Default: `pbkdf2`
    - The hash algorithm to use (`argon2`, `pbkdf2`, `scrypt`, `bcrypt`), `argon2` will spend more memory than others.
- `gitea_users`
    - Default: empty
    - Set of users to be created by the playbook. Check [Users](#users) section below. You can also check [Examples](#examples).

## Users

The `gitea_users` configuration allows the playbook to create users and repositories at deploy time.
This configuration contains a map of users, where the key is the username, and the value is the configuration for a user.

A users configuration includes:
- `email`
    - Required.
    - The email address to set for the user.
- `password`
    - Required.
    - The password to set for the user.
- `admin`
    - Optional, defaults to `false`
    - Whether the user is an admin or not.
- `repos`
    - Optional, defaults to `empty`
    - A map containing repository definitions for a given user. Check [Repositories](#repositories) section below.

## Repositories

Each user in Gitea can have a set of repositories. This playbook allow configuring them using a map where the key is the repository name, and the value is the configuration for that repository.

A repository configuration includes:
- `description`
    - Optional, defaults to the repository name.
    - The description of the repository
- `default_branch`
    - Optional, defaults to `main`.
    - The name of the default branch for the repository.
- `private`
    - Optional, defaults to `false`.
    - Whether the repository is public or private.
- `template`
    - Optional, defaults to `false`.
    - Whether the repository is a template.

## Examples

```
gitea_users:
  example1:
    email: example1@example.com
    password: changeme
    admin: true
    repos:
      test1:
        default_branch: dev
      test2:
        template: true
  example2:
    email: example2@example.com
    password: changeme
    repos:
      test3:
        private: true
      test4:
```
