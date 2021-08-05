def encrypt_cipher_name(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.name_cipher = row.name
        row.save()


def encrypt_cipher_phone(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.phone_cipher = row.phone
        row.save()


def decrypt_cipher_name(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    # db_alias = schema_editor.connection.alias
    # for row in MyModel.objects.using(db_alias).all():
    for row in MyModel.objects.all():
        row.name_cipher = ''
        row.save()


def decrypt_cipher_phone(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    # db_alias = schema_editor.connection.alias
    # for row in MyModel.objects.using(db_alias).all():
    for row in MyModel.objects.all():
        row.phone_cipher = ''
        row.save()
