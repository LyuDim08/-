import requests

class Api:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
    
    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    def users_photos(self, photo_count=5, album_id='profile', extended=1, photo_sizes=1):
        url = 'https://api.vk.com/method/photos.get'
        params = {
           'owner_id': self.id,
           'album_id': album_id,
           'extended': extended,
           'photo_sizes': photo_sizes,
           'count': photo_count
        }
        print('Получение фотографий из ВК...')
        response = requests.get(url, params={**self.params, **params})
        return response.json()
    
    def users_albums(self):
        url = 'https://api.vk.com/method/photos.getAlbums'
        params = {
           'owner_id': self.id,
        }
        response = requests.get(url, params={**self.params, **params})
        return response.json()