import django_filters
from cryptography.fernet import Fernet
from django.db import models
from demo.cipher_field import CipherField


class CipherFieldManager(models.Manager):

    def filter(self, *args, **kwargs):
        print('filter', kwargs)
        if kwargs.get('first_name'):
            menbers = Member.objects.all()
            for menber in menbers:
                if menber.first_name == kwargs.get('first_name'):
                    return menber
            # menber_list = Member.objects.all()
            # menber_filter = UserFilter(kwargs, queryset=menber_list)
            # print(menber_filter)
            # return menber_filter
        return self.get_queryset().filter(*args, **kwargs)

    # def get_queryset(self):
    #     print('get_queryset')
    #     print('self.model', self._hints)
    #     print('self.model', self.model._meta.label, self.name)
    #     menbers = Member.objects.all()
    #     for menber in menbers:
    #         if menber.first_name == self.model.first_name:
    #             return menber
    #     return None


# Create your models here.
class Member(models.Model):
    first_name = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    objects = models.Manager()  # The default manager.
    cipher = CipherFieldManager()  # The Dahl-specific manager.

    def __str__(self):
        return self.first_name

    def filert_cipher_field(self, value):
        menbers = Member.objects.all()
        for menber in menbers:
            if menber.first_name == value:
                return menber
        return None


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


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'phone', ]
