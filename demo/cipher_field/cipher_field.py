from django.db import models
from demo.cipher_field.cipher import Cipher

class CipherField(models.CharField):
    description = 'Encrypt your field'

    def __init__(self, token, *args, **kwargs):
        self.cipher = Cipher(token)
        self.token = token
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def get_db_prep_value(self, value, connection, prepared=False):
        encripted = self.cipher.encrypt(value)
        return encripted

    def from_db_value(self, value, expression, connection):
        decrypt = self.cipher.decrypt(value)
        return decrypt
