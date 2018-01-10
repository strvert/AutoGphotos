import json
import requests

from token_utils import Token_utils
import consts


class Upload:

    def upload(self, path):

        with open(consts.TOKEN_PATH, 'r') as f:
            data_dict = json.load(f)
        user_id = data_dict['user_id']

        tu = Token_utils
        access_token = tu.reget_token()

        headers = {
            'Content-Type': 'image/jpeg',
            'Content-Length': '${LENGTH',
            'Slug': '${FILE}',
        }

        params = (
            ('access_token', '${ACCESS_TOKEN}'),
        )

        with open('path', 'rb') as f:
            data = f

        response = requests.post(consts.ENDPOINT_URL + user_id,
                headers=headers, params=params, data=data)

        response = requests.post('${ENDPOINT}?'
                + 'access_token=${ACCESS_TOKEN}', headers=headers, data=data)

