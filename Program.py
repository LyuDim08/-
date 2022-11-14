import requests
import json
import vk
import yandex
from tqdm import tqdm
from my_token_vk import TOKEN_VK


def dump(var):
    print(json.dumps(var, indent=2, ensure_ascii=False).encode('utf8').decode())


def max_size_photos(all_photos, with_url=True):
    photos = []
    count_likes = []
    for item in all_photos['response']['items']:
        likes_count = item['likes']['count']
        name = str(likes_count)
        if likes_count in count_likes:
            name += "_" + str(item['date'])
        item_photo = {
            'file_name': name + ".jpg"
        }
        max_size = 0
        for size in item['sizes']:
            if size['height'] * size['width'] > max_size:
                max_size = size['height'] * size['width']
                if with_url:
                    item_photo['url'] = size['url']
                item_photo['size'] = size['type']
        photos.append(item_photo)
        count_likes.append(likes_count)
    return photos


def upload_photos_to_yandex(photos, folder_name='Vk'):
    photos_count = len(photos)
    i = 1
    for photo in tqdm(photos):
        ya = yandex.Api(TOKEN_YA)
        result = ya.upload_file(
            folder_name,
            photo['file_name'],
            photo['url']
        )
        i += 1
    print('Загрузка файлов завершена.')


def update_json(photos):
    print('Создание JSON-файла...')
    json_string = json.dumps(photos, indent=4)
    my_file = open("result.json", "w+")
    my_file.write(json_string)
    my_file.close()
    print('Работа программы завершена.')


# Получение фотографий из профиля ВК
user_id = input('Введите ваш ID: ')
vk = vk.Api(TOKEN_VK, user_id)
vk_photos = vk.users_photos(5)

if ('response' in vk_photos) and ('items' in vk_photos['response']):
    # Выборка фотографий наибольшого размера
    photos = max_size_photos(vk_photos)

    # Загрузка фотографий в Яндекс.диск
    TOKEN_YA = input('Введите токен с Полигона Янднекс.Диска:  ')
    folder_name = input('Введите название папки: ')
    upload_photos_to_yandex(photos, folder_name)

    # Обновление JSON-файла с результатами
    update_json(max_size_photos(vk_photos, False))
else:
    print('\033[31m' + 'Ошибка получения фотографий из ВК API' + '\033[0m')
    my_file = open("result.json", "w+")
    my_file.write('[]')
    my_file.close()