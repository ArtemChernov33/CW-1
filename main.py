from config import token_vk, token_yd
from loading_in_yd import upload_file
from vk_info import VkInfo
from vk_photos import get_photo, create_json
from yd_info import YdInfo


def main():
    user_id = input('Введите свой ID:')
    path = input('Введите адрес:')
    count = input('Введите количество фотографий:')
    photos = get_photo(vk, count, user_id)
    create_json(photos)
    upload_file(yd, photos, path)


if __name__ == '__main__':
    vk = VkInfo(token_vk)
    yd = YdInfo(token_yd)
    main()
