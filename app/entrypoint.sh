#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py migrate

python manage.py loaddata dev_user.json --app auths
python manage.py loaddata mock_user.json --app auths
python manage.py loaddata country.json --app accounts
python manage.py loaddata university.json --app accounts
python manage.py loaddata major.json --app accounts
python manage.py loaddata mock_basic_info.json --app accounts

python manage.py collectstatic --no-input --clear
exec "$@"
