# Mercury
Ansible script to deploy Wireguard to and existing server and generate client configs.

Lets make sure we can access the guests.
`ansible -i hosts all -m ping`

To deploy just run.
`zsh ./run.sh`

https://www.cyberciti.biz/faq/ubuntu-20-04-set-up-wireguard-vpn-server/

```
docker create \
    --name nfs-service \
    --mount 'type=volume,source=nfsvolume,target=/app,volume-driver=local,volume-opt=type=nfs,volume-opt=device=:/var/docker-nfs,"volume-opt=o=10.0.0.10,rw,nfsvers=4,async"' \
    nginx:latest
```

sudo mount 10.2.3.10:/mnt/ocean/block_storage/postgres-data /mnt/pgdata

showmount -e ocean.local

sudo mount -t nfs ocean.local:/mnt/ocean/block_storage/postgres-data ~/.mounts/postgres-data
mount -t nfs 192.168.1.88:/mnt/ocean/block_storage/postgres-data ~/.mounts/postgres-data


curl -kI --insecure -X "POST" https://ocean.wg/api/v1.0/sharing/nfs/

{
    "id": 17,
    "nfs_alldirs": false,
    "nfs_comment": "",
    "nfs_enabled": true,
    "nfs_hosts": "192.168.65",
    "nfs_mapall_group": "",
    "nfs_mapall_user": "",
    "nfs_maproot_group": "wheel",
    "nfs_maproot_user": "root",
    "nfs_network": "",
    "nfs_paths": [
        "/mnt/ocean/downloads/usenet"
    ],
    "nfs_quiet": false,
    "nfs_ro": false,
    "nfs_security": []
}

