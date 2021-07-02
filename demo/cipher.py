from cryptography.fernet import Fernet

class Cipher:
  
  def __init__(self, token):
    self.fernet = Fernet(token)

  def encrypt(self, value):
    self.fernet.encrypt(value.encode('utf-8')).decode('utf-8')
    return value

  def decrypt(self, value):
    self.fernet.decrypt(value.encode('utf-8')).decode('utf-8')
    return value

