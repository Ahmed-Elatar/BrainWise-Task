# BrainWise-Task

BrainWise - Project Setup Guide<br/>
Pre-requisites<br/>
Before you begin, ensure you have met the following requirements:
- python_version = "3.10"
- Django = "4.2"
- psycopg2 = "*"
- djangorestframework = "*"
  
1-Install Dependencies :<br/>
- $ pip install django==4.2
- $ pip install psycopg2
- $ pip install djangorestframework


2-Configure Database Settings <br/>
Open settings.py in your Django project directory and update the DATABASES setting to configure your PostgreSQL database. <br/>
Here’s an example configuration:
<br/><br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'your_database_name',<br/>
        'USER': 'your_database_user',<br/>
        'PASSWORD': 'your_database_password',<br/>
        'HOST': 'your_database_host',<br/>
        'PORT': 'your_database_port',<br/>
    }<br/>
}<br/>

<br/>

3-Run commands:<br/>
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
- $ pytohn3 manage.py runserver
- Your project should now be running at http://127.0.0.1:8000/

  .

