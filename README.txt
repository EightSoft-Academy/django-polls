    Model-Url-View-Template
TIPS:
    PART 1 - create project & app
1. $ django-admin startproject polldj
2. $ python manage.py startapp polls
3. $ python manage.py migrate
3. The 'migrate' command looks at the 'INSTALLED_APPS' setting and creates any necessary database tables

    PART 2 - setup db, create model, admin site
4. Then create your models
4. Activating models, with models Django able to:
 - Create a database schema (CREATE TABLE statements) for this app.
 - Create a Python database-access API for accessing 'Question' and 'Choice' objects.
5. Include the app in your project from 'INSTALLED_APPS' list
6. $ python manage.py makemigrations polls
6. $ python manage.py sqlmigrate polls 0001
7. Change your models (in models.py):
 - Run '$ python manage.py makemigrations' to create migrations for those changes
 - Run '$ python manage.py migrate' to apply those changes to the database
8. Playing with the API (models=data): '$ python manage.py shell'
 - https://docs.djangoproject.com/en/3.0/intro/tutorial02/#playing-with-the-api
9. Django Admin
9. Creating an admin user: '$ python manage.py createsuperuser'

    PART 3 - Creating "views"


References:
1. About q.choice_set.all(): https://docs.djangoproject.com/en/3.0/ref/models/relations/
2. About __startswith, __endswith ... https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups-intro
3. Database API: https://docs.djangoproject.com/en/3.0/topics/db/queries/
4. INTERNATIONALIZATION: https://docs.djangoproject.com/en/3.0/topics/i18n/translation/
