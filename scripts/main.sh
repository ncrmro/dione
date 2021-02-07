#!/usr/bin/env bash

ENV=${ENV:-production}
export K8S_AUTH_KUBECONFIG=temp/kubectl-config-${ENV}.yml

poetry run ansible-playbook \
--vault-password-file ~/.ansible/vault/default_key.txt \
-i inventories/${ENV}/hosts.ini \
--tags $1 \
main.yml
