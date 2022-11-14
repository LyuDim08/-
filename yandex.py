import requests

class Api:
    
    def __init__(self, access_token):
        self.headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth ' + access_token
        }
        
    def upload_file(self, folder_name, file_name, url):
        api_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
        'path': folder_name + '/' + file_name, 
        'url': url
        }

        result = self.get_folder(folder_name)
        if 'error' in result:
            self.create_folder(folder_name)
      
        response = requests.post(api_url, params=params, headers=self.headers)
        return response.json()

    def create_folder(self, path):
        api_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
        'path': path, 
        }
        response = requests.put(api_url, params=params, headers=self.headers)
        return response.json()

    def get_folder(self, path):
        api_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
        'path': path, 
        }
        response = requests.get(api_url, params=params, headers=self.headers)
        return response.json()