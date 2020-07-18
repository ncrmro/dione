#!/usr/bin/env zfs

source venv/bin/activate
ansible-playbook -i hosts main.yml
