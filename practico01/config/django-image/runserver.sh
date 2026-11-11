#!/bin/bash

if [ ! -f manage.py ]
then
    django-admin startproject app .
fi

sleep 2

python manage.py makemigrations 
python manage.py migrate --noinput

if [[ ! -z "${DJANGO_SU_NAME}" ]]
then
    echo "from django.contrib.auth.models import User; User.objects.filter(username='${DJANGO_SU_NAME}').exists() or User.objects.create_superuser(username='${DJANGO_SU_NAME}', email='${DJANGO_SU_EMAIL}', password='${DJANGO_SU_PASSWORD}')" | python manage.py shell
fi

python manage.py runserver 0.0.0.0:8000