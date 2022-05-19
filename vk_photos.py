def get_photo(vk, count, user_id):
    params = {
        'user_ids': user_id,
    }
    res = vk.execute_method('users.get', params)
    items = res.json()['response']
    for id in items:
        id_user = id['id']
        params = {
            'owner_id': id_user,
            'album_id': 'profile',
            'extended': 'likes',
            'photo_sizes': '1',
            'count': count
        }
    res = vk.execute_method('photos.get', params)
    res_photo = res.json()['response']['items']
    photos = []
    for photo_info in res_photo:
        photo = {
            'date': str(photo_info['date']),
            'likes': photo_info['likes']['count'],
            'url': photo_info['sizes'][-1]['url'],
            'size': photo_info['sizes'][-1]['type']
        }
        photos.append(photo)

    likes = []
    # TODO TODO переработать в одну строку
    for photo in photos:
        likes.append(photo['likes'])

    non_unique_likes = []
    for like in likes:
        if likes.count(like) > 1 and like not in non_unique_likes:
            non_unique_likes.append(like)

    items = []
    for photo in photos:
        filename = photo['likes']
        if photo['likes'] in non_unique_likes:
            filename = f'{photo["likes"]}_{photo["date"]}'
        item = {
            'filename': f'{filename}.jpg',
            'url': photo['url'],
            'size': photo['size']
        }
        items.append(item)
    return items


def create_json(fotos):
    with open('info.json', 'w') as outfile:
        outfile.write(f'{fotos}\n')
