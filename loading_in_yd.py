import time

from tqdm import tqdm


def upload_file(yd, photos, path):
    headers = {}
    c = 0
    download_YD = []
    create = yd.execute_method_put(f'?path={path}', headers=headers).json()
    folder = create.get('method')
    for photo in photos:
        if folder == 'GET':
            params = {
                "path": f'/{path}/{photo["filename"]}',
                "url": {photo["url"]},
                "overwrite": "true"
            }
            c += 1
            download_YD.append(c)
            res = yd.execute_method_post('upload', params=params, headers=headers).json()
            for i in tqdm(download_YD):
                time.sleep(0.5)
        else:
            print(f'{create["message"]}')
