hukuru-ansible-role-elasticsearch
=========

This role installs and configure elasticsearch on docker.

Requirements
------------

None

Role Variables
--------------

Available variables are listed in default values (see `defaults/main.yml`):

Dependencies
------------

Tested on Centos 7 only

Example Playbook
----------------

```yaml
- hosts: all

  vars:
    docker_users: ['test']

  roles:
    - hukuru-ansible-role-elasticsearch
```

License
-------

BSD

Author Information
------------------

This role was created in by [hukuruIO](https://www.hukuru.io/)
