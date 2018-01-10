import webbrowser
import requests
import json

import consts


class Token_utils:


    def get_token(self):
        print("クライアントIDを入力してください。(CLIENT ID)")
        client_id = input()
        print("クライアントシークレットを入力してください。(CLUENT SECRET)")
        client_secret = input()

        webbrowser.open("https://accounts.google.com/o/oauth2/v2/auth"
                + "?response_type=code&client_id=" + client_id
                + "&redirect_uri=" + consts.REDIRECT_URI + "&scope=" + consts.PICASA_URL
                + "&access_type=offline")

        print("ブラウザ上に表示されたコードを入力してください。(AUTHORIZATION CODE)")
        auth_code = input()

        params = {
                'code': auth_code,
                'client_id': client_id,
                'client_secret': client_secret,
                'redirect_uri': consts.REDIRECT_URI,
                'grant_type': 'authorization_code',
                'access_type': 'offline',
                }
        r = requests.post(consts.TOKEN_URL, data=params)

        r_dict = r.json()
        access_token = r_dict['access_token']
        refresh_token = r_dict['refresh_token']

        client_dict = {
                'client_id': client_id,
                'client_secret': client_secret,
                'refresh_token': refresh_token
                }

        return client_dict

    def reget_token(self):

        with open(consts.TOKEN_PATH, 'r') as f:
            param_dict = json.load(f)

        params = {
                'refresh_token': param_dict['refresh_token'],
                'client_id': param_dict['client_id'],
                'client_secret': param_dict['client_secret'],
                'grant_type': 'refresh_token'
                }
        r = requests.post(consts.TOKEN_URL, data=params)
        r_dict = r.json()
        access_token = r_dict['access_token']

        return(access_token)



