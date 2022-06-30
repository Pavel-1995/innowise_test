python manage.py migrate --noinput


if [ "$DJANGO_SUPERUSER_NAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_NAME \
        --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py runserver 0.0.0.0:8000
$@

