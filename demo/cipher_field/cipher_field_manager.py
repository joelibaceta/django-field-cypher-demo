from django.db import models
from demo.cipher_field.cipher import Cipher


class CipherFieldManager(models.Manager):

    
    # def get(self, *args, **kwargs):

    #     print("*args")
    #     print(self.__class__)
    #     print(super().__class__)

    #     fields = [
    #         kwarg.split('__')[0]
    #         for kwarg in kwargs.keys()
    #         if kwarg.split('__')[0] in self.model.cipher_fields and len(kwarg.split('__')) == 1
    #     ]

    #     print(self.get_queryset().values('id', *fields))

    #     return super().get(*args, **kwargs)

    def filter(self, *args, **kwargs):

        print("super")
        print(self.__class__)
        
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

            print(kwargs)

        return super().filter(*args, **kwargs)