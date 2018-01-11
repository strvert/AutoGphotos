import json
import requests
import os

from token_utils import Token_utils
import consts


class Upload:

    file_types = {
            '.jpeg': 'image/jpeg',
            '.jpg': 'image/jpeg',
            '.gif': 'imgae/gif',
            '.bmp': 'image/bmp',
            '.3gpp': 'video/3gpp',
            '.avi': 'video/avi',
            '.mov': 'video/quicktime',
            '.qt': 'video/quicktime',
            '.mp4': 'video/mp4',
            '.m4a': 'video/mp4',
            '.mpg': 'video/mpeg',
            '.webm': 'video/webm'
            }

    def upload(self, path):

        with open(consts.TOKEN_PATH, 'r') as f:
            self.data_dict = json.load(f)
        self.user_id = self.data_dict['user_id']

        self.tu = Token_utils()
        self.access_token = self.tu.reget_token()

        headers = {
            'Content-Type': self.file_types[os.path.splitext(path)[1]],
            'Content-Length': str(os.path.getsize(path)),
            'Slug': path,
        }
        print('uploading...')
        print(self.file_types[os.path.splitext(path)[1]])

        params = (
            ('access_token', self.access_token),
        )

        with open(path, 'rb') as f:
            data = f.read()

        response = requests.post(consts.ENDPOINT_URL + self.user_id,
                headers=headers, params=params, data=data)

        return response
