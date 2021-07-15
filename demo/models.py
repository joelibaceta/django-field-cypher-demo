from django.db import models
from demo.cipher_field import CipherField


class CipherFieldManager(models.Manager):

    def filter(self, *args, **kwargs):
        fields = [
            kwarg.split('__')[0]
            for kwarg in kwargs.keys()
            if kwarg.split('__')[0] in self.model.cipher_fields and len(kwarg.split('__')) == 1
        ]
        if len(fields) > 0:
            values = [
                kwargs[field]
                for field in fields
            ]

            data = self.get_queryset().values('id', *fields)

            matched_ids = []
            data_to_match = zip(fields, values)
            for entry in data:
                # for field in fields:
                #     entry[field] = cipher.decrypt(entry[field])

                if all(entry[field] == value for field, value in data_to_match):
                    matched_ids.append(entry['id'])

            for field in fields:
                kwargs.pop(field)

            kwargs['id__in'] = matched_ids

        return super().filter(*args, **kwargs)


# Create your models here.
class Member(models.Model):
    first_name = CipherField(max_length=255, token=b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    objects = models.Manager()  # The default manager.
    cipher = CipherFieldManager()  # The Chiper-specific manager.
    cipher_fields = ['first_name', ]

    def __str__(self):
        return self.first_name

    # Filter the format basic and slow
    def filert_cipher_field(self, value):
        menbers = Member.objects.all()
        for menber in menbers:
            if menber.first_name == value:
                return menber
        return None
