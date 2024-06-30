default: serve

venv_bin := "./.venv/bin"
python := venv_bin / "/python"
pip := venv_bin / "/pip"

venv:
    @[ -d .venv ] || python -m venv .venv

install: venv
    {{ pip }} install -r requirements.txt

pg:
    @if [[ -z "$(docker compose ps -q)" ]]; then docker compose up -d; fi

migrate: pg venv
    {{ python }} manage.py makemigrations && {{ python }} manage.py migrate

test: pg
    {{ python }} manage.py test

serve: pg
    {{ python }} manage.py runserver

freeze:
    {{ pip }} freeze --local > requirements.txt

format:
    {{ venv_bin }}/ruff --fix .
