"""htc_api.api"""

import requests


class Client:
    def __init__(self, username, server_code, url='http://167.99.167.17', port=51337):
        url = 'http://localhost'
        self.username = username
        self.server_code = server_code

        url = url[:-1] if url.endswith('/') else url
        self.base_url = '{}:{}/'.format(url, str(port))

        self.session = requests.Session()
        self.session.headers['Content-Type'] = 'application/json'

    def _request(self, method, uri, payload=None):
        response = self.session.request(method, self.base_url + uri, json=payload)
        response.raise_for_status()
        return response.json()

    def validate(self, server_code=None):
        server_code = self.server_code if not server_code else server_code
        payload = {
            'server_code': self.server_code
        }
        return self._request('GET', 'validate', payload)

    def score(self, username=None):
        username = self.username if not username else username
        return self._request('GET', 'score/' + username)

    def solve(self, level_id, flag):
        payload = {
            'level_id': level_id,
            'flag': flag
        }
        return self._request('GET', 'solve', payload)
