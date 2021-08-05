# django-field-cypher-demo

An experiment about building a custom encrypted field

1. Drop all migrations and db sqlite3
2. Execute commads

 ``` shell
 python manage.py makemigrations
 python manage.py migrate
 python manage.py loaddata person.json
 python manage.py createsuperuser 
 python manage.py makemigrations --empty demo

 ```

3. Copy and paste this extrac code in migration empty create

```python
from django.db import migrations

from demo.cipher_migrate import encrypt_cipher_name, encrypt_cipher_phone, decrypt_cipher_name, decrypt_cipher_phone


class Migration(migrations.Migration):
    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(encrypt_cipher_name, decrypt_cipher_name),
        migrations.RunPython(encrypt_cipher_phone, decrypt_cipher_phone),
    ]
```

6. execute the migrate create manual

```shell
 python manage.py migrate
```

7. Validate this value is cipher in database using viewers database sqlite
8. Visualise your info in admin

9. Rollback migration to 0001
 ```shell
 python manage.py migrate demo 0001
```