# BrainWise-Task

BrainWise - Project Setup Guide
Pre-requisites
Before you begin, ensure you have met the following requirements:
- python_version = "3.10"
- Django = "4.2"
- psycopg2 = "*"
- djangorestframework = "*"

1-Install Dependencies :
-$ pip install django==4.2
-$ pip install psycopg2
-$ pip install djangorestframework


2-Configure Database Settings 
Open settings.py in your Django project directory and update the DATABASES setting to configure your PostgreSQL database. Here’s an example configuration:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    }
}



3-Run commands:
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
- $ pytohn3 manage.py runserver
- Your project should now be running at http://127.0.0.1:8000/

  .

