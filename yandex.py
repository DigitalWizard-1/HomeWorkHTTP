import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        load_dict = response.json()
        href = load_dict.get("href", "")
        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()

if __name__ == '__main__':
    TOKEN = ""
    path_to_file = "test.txt"
    uploader = YaUploader(token=TOKEN)
    uploader.upload(path_to_file)
