from django.db import models
from demo.cipher_field.cipher_field import CipherField, CipherCharField, CipherTextField
from demo.cipher_field.cipher_field_manager import CipherFieldManager


# Create your models here.
class Member(models.Model):
    first_name = CipherCharField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    last_name = CipherCharField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    objects = models.Manager()  # The default manager.
    cipher = CipherFieldManager()  # The Chiper-specific manager.
    cipher_fields = ['first_name', 'last_name']
    objects = CipherFieldManager()

    def __str__(self):
        return self.first_name


class Person(models.Model):
    # name = models.CharField(max_length=255, )
    email = models.EmailField()
    # phone = models.CharField(max_length=255, )
    # name = CipherCharField(max_length=255, blank=True, )
    # phone = CipherCharField(max_length=255, blank=True, )
    name = CipherTextField(max_length=2000, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=', )
    phone = CipherTextField(max_length=2000, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=', )
    objects = models.Manager()  # The default manager.
    cipher_fields = ['name', 'phone']
    objects = CipherFieldManager()  # Custom manager

    def __str__(self):
        return self.name
