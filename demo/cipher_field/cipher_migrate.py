
from demo.cipher_field.cipher import Cipher

def encrypt_all_field(apps, schema_editor):
    cipher = Cipher(b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    MyModel = apps.get_model('demo', 'Person')

    fields_name = [field.name for field in MyModel._meta.get_fields()]
    fields_type = [field.get_internal_type() for field in MyModel._meta.fields]
    for row in MyModel.objects.all():
        for field, type in zip(fields_name, fields_type):
            if type == 'CipherField':
                setattr(row, field, cipher.encrypt(str(getattr(row, field))))
        row.save()


def decrypt_all_field(apps, schema_editor):
    cipher = Cipher(b'mi84uq0CPvQF1hPbU-pbXy3uKr1iRgSgw1D24vZ_5tA=')
    MyModel = apps.get_model('demo', 'Person')

    fields_name = [field.name for field in MyModel._meta.get_fields()]
    fields_type = [field.get_internal_type() for field in MyModel._meta.fields]
    for row in MyModel.objects.all():
        for field, type in zip(fields_name, fields_type):
            if type == 'CipherField':
                setattr(row, field, cipher.decrypt(str(getattr(row, field))))
        row.save()
