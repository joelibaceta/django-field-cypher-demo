
def cipher_name(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.name_cipher =  row.name
        row.save()

def cipher_phone(apps, schema_editor):
    MyModel = apps.get_model('demo', 'Person')
    for row in MyModel.objects.all():
        row.phone_cipher =  row.phone
        row.save()
