from cryptography.fernet import Fernet


class Cipher:

    def __init__(self, token):
        self.fernet = Fernet(token)

    def encrypt(self, value):
        if value is None:
            return value
        return self.fernet.encrypt(value.encode('utf-8')).decode('utf-8')

    def decrypt(self, value):
        if value is None:
            return value
        try:
            decrypt = self.fernet.decrypt(value.encode('utf-8')).decode('utf-8')
        except Exception as msg:
            # print("Can't decrypt: ", msg)
            return value
        return decrypt
