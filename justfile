default: serve

migrate: pg
    python manage.py makemigrations && python manage.py migrate

test: pg
    python manage.py test

pg:
    docker compose up -d

serve: pg
    python manage.py runserver
