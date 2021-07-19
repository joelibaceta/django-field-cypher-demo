from cryptography.fernet import Fernet


class Cipher:

    def __init__(self, token):
        self.fernet = Fernet(token)

    def encrypt(self, value):
        encrypt = self.fernet.encrypt(value.encode('utf-8')).decode('utf-8')
        return encrypt

    def decrypt(self, value):
        try:
            decrypt = self.fernet.decrypt(value.encode('utf-8')).decode('utf-8')
        except Exception as msg:
            # print("Can't decrypt: ", msg)
            return None
        return decrypt
