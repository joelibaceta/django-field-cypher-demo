from django.db import models
from demo.cipher import Cipher


# class CipherField(models.CharField):
#
#   def __init__(self, *args, **kwargs):
#     self.cipher = Cipher(kwargs["token"])
#     kwargs.pop("token", None)
#     super().__init__(*args, **kwargs)
#
#   def from_db_value(self, value, expression, connection):
#     c_value = self.cipher.decrypt(value)
#     return c_value
#
#   # def get_lookup(self, lookup_name):
#   #   if lookup_name == 'exact':
#   #     return 'exact'
#   #   elif lookup_name == 'in':
#   #     return 'in'
#   #   elif lookup_name == 'isnull':
#   #     return 'isnull'
#   #   else:
#   #     return super().get_lookup(lookup_name)
#
#
#   def get_prep_value(self, value):
#     if value is None or value == '':
#       return None
#
#     return self.cipher.encrypt(value)
#
#   def to_python(self, value):
#     if value is None:
#       return value
#
#     return self.cipher.decrypt(value)
#

class CipherField(models.CharField):
    description = 'My cyper value'

    def __init__(self, *args, **kwargs):
        self.cipher = Cipher(kwargs['token'])
        print("token", kwargs['token'])
        kwargs.pop('token', None)
        super().__init__(*args, **kwargs)

    # def get_lookup(self, lookup_name):
    #     print('get_lookup', lookup_name)
    #
    #     # if lookup_name == 'icontains':
    #     #     return self.get_prep_value(value)
    #     return lookup_name

    # def get_prep_value(self, value):
    #     if value is None or value == '':
    #         return None
    #     return self.cipher.encrypt(value)

    def get_transform(self, name):
        print('get_transform', name)
        return name

    # def get_prep_lookup(self, lookup_type, value):
    #     print('get_prep_lookup ', value)
    #     print('get_prep_lookup ', lookup_type)
    #     if lookup_type == 'exact':
    #         return self.get_prep_value(value)
    #     elif lookup_type == 'in':
    #         return [self.get_prep_value(v) for v in value]
    #     else:
    #         raise TypeError('Lookup type %r not supported.' % lookup_type)

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        print('get_db_prep_value', value)
        encripted = self.cipher.encrypt(value)
        print('get_db_prep_value encripted', encripted)
        return encripted

    def to_python(self, value):
        print("to_python", value)
        # encrypt = self.cipher.encrypt(value)
        # print("to_python encrypt", encrypt)
        return super().to_python(value)

    #
    # def get_db_prep_save(self, value, connection):
    #     print('get_db_prep_save', value)
    #     encripted = self.cipher.encrypt(value)
    #     print('get_db_prep_save encripted', encripted)
    #     return encripted

    def from_db_value(self, value, expression, connection):
        print("from_db_value", value)
        decrypt = self.cipher.decrypt(value)
        print("from_db_value decrypt", decrypt)
        return decrypt
