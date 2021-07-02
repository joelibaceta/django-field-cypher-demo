from django.db import models
from cryptography.fernet import Fernet

class CipherField(models.CharField):

  def __init__(self, *args, **kwargs):
    fernet = Fernet(kwargs["token"])
    self.fernet = fernet
    kwargs.pop("token", None)
    super().__init__(*args, **kwargs)

  def from_db_value(self, value, expression, connection):
    c_value = self.fernet.decrypt(value.encode('utf-8')).decode('utf-8')
    return c_value
  
  def get_prep_lookup(self, lookup_type, value):
        # We only handle 'exact'  
        if lookup_type == 'exact':
            return self.get_prep_value(value)
        else:
            raise TypeError('Lookup type %r not supported.' % lookup_type)
            
  def get_prep_value(self, value): 
    value = super().get_prep_value(value)
    c_value = self.fernet.encrypt(value.encode('utf-8')).decode('utf-8')
    return c_value

  def to_python(self, value): 
    #print(value)
    c_value = self.fernet.decrypt(value.encode('utf-8')).decode('utf-8')
    return c_value