import requests


class YdInfo:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers_default = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        self.params_default = {
            "overwrite": "true"
        }

    def execute_method_put(self, method, headers):
        url = self.base_url + method
        headers.update(self.headers_default)
        return requests.put(url, headers=headers)

    def execute_method_post(self, method, params, headers):
        url = self.base_url + method
        headers.update(self.headers_default)
        params.update(self.params_default)
        return requests.post(url, params=params, headers=headers)
