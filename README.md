# Requirements

1. [direnv](https://direnv.net/)  
1. [devenv](https://devenv.sh/)

# Development environment

1. run `direnv allow` to permit auto-activation of the `devenv` shell. (you only need to do this once)
1. launch `nvim` or `code` from the active `devenv` shell.
1. start services (postgres, etc) `devenv up`
1. start the development server with `django-admin runserver`

