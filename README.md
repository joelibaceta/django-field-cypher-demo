# django-field-cypher-demo

An experiment about building a custom encrypted field

1. Drop all migrations and db sqlite3
2. Execute commads

 ``` shell
 python manage.py makemigrations
 python manage.py migrate
 python manage.py loaddata person.json
 python manage.py createsuperuser 
 ```

3. In folder migrations the project demo create file and name 0002_migrate_cipher.py
4. Copy and paste this extrac code

```python
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

```

5. execute the migrate create manual

```shell
 python manage.py migrate
```

6. Validate this value is cipher in database using viewers database sqlite
7. Visualise your info in admin
 