# OpenKin.io

## Requirements

1. [direnv](https://direnv.net/)  
1. [devenv](https://devenv.sh/)

## Development environment

- run `direnv allow` to permit auto-activation of the `devenv` shell. (you only need to do this once)
- launch your editor from the active `devenv` shell.

## Dev server

- start services (postgres, etc) `devenv up`
- start the development server with `python manage.py runserver` (you may need to run perform database migrations first)
