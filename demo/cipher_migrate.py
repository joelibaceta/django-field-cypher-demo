from django.db import transaction

from demo.cipher_field.cipher import Cipher
from demo.cipher_field.cipher_field import CipherField
from demo.models import Person

from demo.cipher_field.cipher_field import CipherField
from demo.models import Person


def encrypt_all_field(apps, schema_editor):
    cipher = Cipher(b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.name = cipher.encrypt(str(row.name))
        row.phone = cipher.encrypt(str(row.phone))
        row.save()

def decrypt_all_field(apps, schema_editor):
    cipher = Cipher(b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.name = cipher.decrypt(str(row.name))
        row.phone = cipher.decrypt(str(row.phone))
        row.save()

    # fields = [field.name for field in MyModel._meta.get_fields()]
    # field_type = [field.get_internal_type() for field in MyModel._meta.fields]
    # field_match = zip(fields, field_type)
    # data = MyModel.objects.all()
    # for entry in data:
    #     for field, type in field_match:
    #         print(field, type)
    #         print(entry)
    #         if type == 'CipherField':
    #             entry[field] = cipher.encrypt(str(entry[field]))
    #             print(entry[field])
    #     entry.save()


# def encrypt_cipher_name(apps, schema_editor):
#     MyModel = apps.get_model('demo', 'Person')
#     for row in MyModel.objects.all():
#         row.name_cipher = row.name
#         row.save()
#
#
# def encrypt_cipher_phone(apps, schema_editor):
#     MyModel = apps.get_model('demo', 'Person')
#     for row in MyModel.objects.all():
#         row.phone_cipher = row.phone
#         row.save()
#
#
# def decrypt_cipher_name(apps, schema_editor):
#     MyModel = apps.get_model('demo', 'Person')
#     # db_alias = schema_editor.connection.alias
#     # for row in MyModel.objects.using(db_alias).all():
#     for row in MyModel.objects.all():
#         row.name_cipher = ''
#         row.save()
#
#
# def decrypt_cipher_phone(apps, schema_editor):
#     MyModel = apps.get_model('demo', 'Person')
#     # db_alias = schema_editor.connection.alias
#     # for row in MyModel.objects.using(db_alias).all():
#     for row in MyModel.objects.all():
#         row.phone_cipher = ''
#         row.save()
