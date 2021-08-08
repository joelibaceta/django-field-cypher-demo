# django-field-cypher-demo

An experiment about building a custom encrypted field

1. Drop all migrations and db sqlite3
2. Execute commads

 ``` shell
 python manage.py makemigrations
 python manage.py migrate
 python manage.py loaddata person.json
 python manage.py createsuperuser --username yahyr --email yahyr@gmail.com
```
 
7. Validate this value is cipher in database using viewers database sqlite
8. Visualise your info in admin

9. Rollback migration to 0001

 ```shell
 python manage.py migrate demo 0001
```

 