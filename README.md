# DJORNADO template application
* included: tornado; peewee orm; django-styled migrations; protobuf api; auth; tests
## Migrations
* make migrations: python manage.py makemigrations [name]
* run migrations: python manage.py migrate [name]
* rollback migration: python manage.py rollback name
## Tests
* running: py.test
* coverage: py.test --cov=project --cov-config .coveragec
## Application
* running: python manage.py runserver
## Protobuf
* protoc -I project/application/proto/ --python_out=project/application/ project/application/proto/models.proto
