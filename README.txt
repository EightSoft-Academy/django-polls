    Model-Url-View-Template
TIPS:
1. $ django-admin startproject polldj
2. $ python manage.py startapp polls
3. $ python manage.py migrate
3. The 'migrate' command looks at the 'INSTALLED_APPS' setting and creates any necessary database tables
4. Then create your models
4. Activating models, with models Django able to:
 - Create a database schema (CREATE TABLE statements) for this app.
 - Create a Python database-access API for accessing 'Question' and 'Choice' objects.
5. Include the app in your project from 'INSTALLED_APPS' list
6. $ python manage.py makemigrations polls
6. $ python manage.py sqlmigrate polls 0001
