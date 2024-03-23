{ pkgs, ... }:

{
  dotenv.enable = true;

  packages = [
    pkgs.djlint
    pkgs.gettext
    pkgs.just
    pkgs.marksman
    pkgs.ruff
    pkgs.ruff-lsp
    pkgs.tailwindcss
  ];

  languages.python.enable = true;
  languages.python.venv.enable = true;
  languages.python.venv.requirements = "-r ${./requirements.txt}";

  difftastic.enable = true;

  services.postgres = {
    enable = true;
    package = pkgs.postgresql_16;
    initialDatabases = [{ name = "openkin_db"; }];
    initialScript = "create role postgres superuser; alter role postgres with login;";
    # can add extensions in the future if needed
    # https://devenv.sh/reference/options/#servicespostgresextensions
  };

  pre-commit = {
    excludes = [
      ".*/migrations/.*"
    ];
    hooks = {
      nixpkgs-fmt.enable = true;
      ruff.enable = true;
      djlint = {
        enable = true;
        name = "djlint-reformat-django";
        files = ".*/templates/.*\.html$";
        entry = "${pkgs.djlint}/bin/djlint --reformat --profile django --configuration ${./pyproject.toml}";
      };
    };
  };
}
