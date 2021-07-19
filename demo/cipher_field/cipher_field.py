from django.db import models
from demo.cipher_field.cipher import Cipher

class CipherField(models.CharField):
    description = 'Encrypt your field'

    def __init__(self, *args, **kwargs):
        self.cipher = Cipher(kwargs['token'])
        self.token = kwargs['token']
        kwargs.pop('token', None)
        super().__init__(*args, **kwargs)

    def get_db_prep_value(self, value, connection, prepared=False):
        encripted = self.cipher.encrypt(value)
        return encripted

    def from_db_value(self, value, expression, connection):
        decrypt = self.cipher.decrypt(value)
        return decrypt
