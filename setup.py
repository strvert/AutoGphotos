import webbrowser
import requests
import json

REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"
PICASA_URL = "https://picasaweb.google.com/data/"
TOKEN_URL = "https://www.googleapis.com/oauth2/v4/token"

TOKEN_PATH = ".token.json"

print("クライアントIDを入力してください。(CLIENT ID)")
client_id = input()

print("クライアントシークレットを入力してください。(CLUENT SECRET)")
client_secret = input()

webbrowser.open("https://accounts.google.com/o/oauth2/v2/auth"
        + "?response_type=code&client_id=" + client_id
        + "&redirect_uri=" + REDIRECT_URI + "&scope=" + PICASA_URL
        + "&access_type=offline")

print("ブラウザ上に表示されたコードを入力してください。(AUTHORIZATION CODE)")
auth_code = input()

params = {
        'code': auth_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
        'access_type': 'offline',
        }

r = requests.post(TOKEN_URL, data=params)
r_dict = r.json()

with open(TOKEN_PATH, 'w') as f:
    json.dump(r_dict, f, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
