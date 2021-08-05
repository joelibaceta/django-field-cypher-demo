from django.db import migrations

from demo.cipher_migrate import cipher_name, cipher_phone


class Migration(migrations.Migration):
    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(cipher_name),
        migrations.RunPython(cipher_phone),
    ]