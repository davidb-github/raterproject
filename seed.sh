#!/bin/bash

rm -rf raterapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations raterapi
python manage.py migrate raterapi
python manage.py loaddata events
python manage.py loaddata gamers
python manage.py loaddata games
python manage.py loaddata gametypes
python manage.py loaddata tokens