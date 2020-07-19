# This script should initialize all parts related to media aka DIONE,

import requests

host = "https://ocean.wg"


nfs_shares_res = requests.get(
    f'{host}/api/v1.0/sharing/nfs/',
    auth=('root', '!&Nas699*'), verify=False
).json()

current_shares = [s['nfs_paths'][0] for s in nfs_shares_res]
print(current_shares)

datasets_res = requests.get(
    f'{host}/api/v1.0/storage/dataset/?limit=200',
    auth=('root', '!&Nas699*'), verify=False
).json()


# share all datasets in specified list

# for ds in requests.get(
#     f'{host}/api/v1.0/sharing/nfs/?limit=200',
#     auth=('root', '!&Nas699*'), verify=False
# ).json():
#     datasets_res = requests.delete(
#         f'{host}/api/v1.0/sharing/nfs/{ds["id"]}',
#         auth=('root', '!&Nas699*'), verify=False,
#     ).json()
#
for ds in datasets_res:
    mp = ds['mountpoint']
    if '/mnt/ocean/media/' in mp or '/mnt/ocean/block_storage/' in mp or '/mnt/ocean/downloads/' in mp:
        if mp not in current_shares:
            print("need to create mountpoint!")
            datasets_res = requests.post(
                f'{host}/api/v1.0/sharing/nfs/',
                auth=('root', '!&Nas699*'), verify=False,
                json=dict(
                    nfs_paths=[mp],
                    nfs_hosts="192.168.1.65",
                    nfs_maproot_user="root",
                    nfs_maproot_group="wheel",
                    nfs_security=[]
                )
            ).json()

            print(datasets_res)
