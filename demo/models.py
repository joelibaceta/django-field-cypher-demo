from cryptography.fernet import Fernet
from django.db import models
from demo.cipher_field import CipherField

# Create your models here.
class Member(models.Model):
  
  first_name = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=12)

  # def get(self, *args, **kwargs):
  #   fernet = Fernet('1rbDtUldG5WVoqdf-k22bptH2td6fiwylEeSNXa9tFw=')
  #   dec_message = fernet.decrypt(self.__dict__["first_name"].encode('utf-8')).decode('utf-8')
  #   self.first_name=dec_message
  #   super(Member, self).get(*args, **kwargs)

  # def __setattr__(self, attr, value):
  #   fernet = Fernet('1rbDtUldG5WVoqdf-k22bptH2td6fiwylEeSNXa9tFw=')
  #   if attr == 'first_name':
  #     c_first_name = fernet.encrypt(value.encode('utf-8')).decode('utf-8')
  #     super().__setattr__('first_name', c_first_name)
  #   else:
  #     super().__setattr__(attr, value)

  # def __getattr__(self, attr):
  #   fernet = Fernet('1rbDtUldG5WVoqdf-k22bptH2td6fiwylEeSNXa9tFw=')
  #   dec_message = fernet.decrypt(self.__dict__[attr].encode('utf-8')).decode('utf-8')
  #   return dec_message