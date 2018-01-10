from token_utils import Token_utils


class Upload:

    def upload(self, path):
        tu = Token_utils
        access_token = tu.reget_token()

