[![CI](https://github.com/peering-manager/ansible-role-peering-manager/workflows/CI/badge.svg?event=push)](https://github.com/peering-manager/ansible-role-peering-manager/actions?query=workflow%3ACI)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-peering--manager-blue.svg)](https://galaxy.ansible.com/gmazoyer/peering_manager)

# Ansible Role: Peering Manager

An Ansible Role that installs Peering Manager on Debian/Ubuntu.

This role install all dependencies required by Peering Manager including the
PostgreSQL database. So it can be used to setup Peering Manager as an appliance
including everything in the same machine.

Web backend and frontend setups can be disabled if you already have your own
way to handle them.

## Dependencies

None.

## Roles Variables

Available variables are listed below, along with default values:

Setup for the PostgreSQL database:

    peering_manager_database: peering-manager
    peering_manager_database_user: peering-manager
    peering_manager_database_password: peering-manager
    peering_manager_database_host: localhost # This will force PostgreSQL to be setup

Where to get Peering Manager and which version:

    peering_manager_version: 1.4.5
    peering_manager_git_url: https://github.com/peering-manager/peering-manager.git

Where to install Peering Manager:

    peering_manager_install_directory: /opt/peering-manager

The username, password and email for the super user.

    peering_manager_superuser_username: admin
    peering_manager_superuser_password: admin
    peering_manager_superuser_email: admin@example.com

Extra Python packages can be listed in order for this role to install them in
the virtual environment:

    peering_manager_local_requirements: []

LDAP can be used as authentication mechanism. It must be enabled, and the whole
LDAP configuration has to be provided in the following variables (see Peering
Manager
[documentation](https://peering-manager.readthedocs.io/en/latest/setup/ldap/)):

    peering_manager_setup_ldap_auth: false
    peering_manager_ldap_config: ""

The configuration for Peering Manager must be given as `key: value` pairs like
the following, please note that the secret key does not need to be given as it
will be generated automatically:

    peering_manager_config:
      ALLOWED_HOSTS:
        - localhost
        - 127.0.0.1
      MY_ASN: 201281
      TIME_ZONE: "Europe/Paris"
      …

Configuration for the backend web server and systemd:

    peering_manager_setup_systemd: false
    peering_manager_gunicorn_address: 127.0.0.1
    peering_manager_gunicorn_port: 8001
    peering_manager_gunicorn_workers_number: 5

Whether or not to configure the frontend web server:

    peering_manager_setup_web_frontend: false

## Example Playbook

    - hosts: peering_manager
      roles:
        - { role: gmazoyer.peering_manager }

## License

This Ansible Role is released under the terms of the GNU GPLv3. Please read
the LICENSE file for more information.

## Author Information

This role was created in 2019 by [Guillaume Mazoyer](https://mazoyer.eu).
