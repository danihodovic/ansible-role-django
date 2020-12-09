# ansible-role-django [![Build Status](https://ci.depode.com/api/badges/danihodovic/ansible-role-django/status.svg)](https://ci.depode.com/danihodovic/ansible-role-django)

Deploys Django as a Docker container

Example playbook
```yaml
- name: Deploy django app
  hosts: main
  tasks:
    - name: Clone my Django repository
      git:
        repo: >-
          https://{{ my_gitlab_deployment_user }}:{{ my_gitlab_deployment_token }}@gitlab.com/organization/my_website.git
        dest: /opt/my_website
        depth: 1

    - name: Deploy app
      import_role:
        name: ansible-role-django
      vars:
        django_dir: /opt/my_website/
        django_docker_container:
          name: my_website
          env:
            DJANGO_SECRET_KEY: '{{ vault_my_website_django_secret_key }}'
            DJANGO_ADMIN_URL: secret-admin-url
            DATABASE_URL: 'postgres://{{ postgres_user }}:{{ vault_postgres_password }}@postgres/my_database'
          networks:
            - name: nginx
            - name: db
```
