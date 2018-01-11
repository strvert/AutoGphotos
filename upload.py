import json
import requests
import os

from token_utils import Token_utils
import consts


class Upload:

    def upload(self, path):

        with open(consts.TOKEN_PATH, 'r') as f:
            data_dict = json.load(f)
        user_id = data_dict['user_id']

        tu = Token_utils
        access_token = tu.reget_token()

        images = {
                'jpeg',
                'png',
                'gif',
                'webp'
                }

        videos = {
                }

        headers = {
            'Content-Type': 'image/jpeg',
            'Content-Length': os.path.getsize(path),
            'Slug': path,
        }

        params = (
            ('access_token', access_token),
        )

        with open('path', 'rb') as f:
            data = f

        response = requests.post(consts.ENDPOINT_URL + user_id,
                headers=headers, params=params, data=data)

        return response
