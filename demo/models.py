from django.db import models
from demo.cipher_field.cipher_field import CipherField
from demo.cipher_field.cipher_field_manager import CipherFieldManager


# Create your models here.
class Member(models.Model):
    first_name = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    last_name = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    objects = models.Manager()  # The default manager.
    cipher = CipherFieldManager()  # The Chiper-specific manager.
    cipher_fields = ['first_name', 'last_name']
    objects = CipherFieldManager()

    def __str__(self):
        return self.first_name


class Person(models.Model):
    name = models.CharField(max_length=255, )
    phone = models.CharField(max_length=255, )
    name_cipher = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=', blank=True, )
    phone_cipher = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=', blank=True, )
    objects = models.Manager()  # The default manager.
    cipher_fields = ['name_cipher', 'phone_cipher']
    objects = CipherFieldManager()  # Custom manager

    def __str__(self):
        return self.name
