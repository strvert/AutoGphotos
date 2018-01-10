import json

from token_utils import Token_utils
import consts

tu = Token_utils()
data_dict = tu.get_token()

print('先程ブラウザで選択したGoogleアカウントのUserIDもしくはGmail Addressを入力してください。(UserID or EmailAddress)')
user_id = input()
data_dict["user_id"] = user_id

with open(consts.TOKEN_PATH, 'w') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4,
            sort_keys=True, separators=(',', ': '))

print("セットアップが完了しました。(Successfully.)")
