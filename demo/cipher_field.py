from django.db import models
from demo.cipher import Cipher


class CipherField(models.CharField):

  def __init__(self, *args, **kwargs):
    self.cipher = Cipher(kwargs["token"])
    kwargs.pop("token", None)
    super().__init__(*args, **kwargs)

  def from_db_value(self, value, expression, connection):
    c_value = self.cipher.decrypt(value)
    return c_value
  
  # def get_lookup(self, lookup_name):
  #   if lookup_name == 'exact':
  #     return 'exact'
  #   elif lookup_name == 'in':
  #     return 'in'
  #   elif lookup_name == 'isnull':
  #     return 'isnull'
  #   else:
  #     return super().get_lookup(lookup_name)
      
            
  def get_prep_value(self, value): 
    if value is None or value == '':
      return None
    
    return self.cipher.encrypt(value)

  def to_python(self, value): 
    if value is None:
      return value
  
    return self.cipher.decrypt(value)