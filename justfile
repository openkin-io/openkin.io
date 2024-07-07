default: serve

venv_bin := "./.venv/bin"
python := venv_bin / "/python"
pip := venv_bin / "/pip"

compose:
    @if [[ -z "$(docker compose ps -q)" ]]; then docker compose up -d; fi

migrate: compose
    docker compose exec django python manage.py makemigrations && docker compose exec django python manage.py migrate

test: compose
    docker compose exec django python manage.py test

serve: compose

freeze:
    {{ pip }} freeze --local | sort --ignore-case > requirements.txt

venv:
    @if [[! -d ".venv" ]]; then python -m venv .venv; fi

format: venv
    {{ venv_bin }}/ruff --fix .
