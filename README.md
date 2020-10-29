# Pipenv Intro
A small intro to Pipenv

### Installing
Run `pip install --user pipenv` to install Pipenv. Alternatively, follow [these instructions](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
### Files
- **Pipfile**: The main configuration file for pipenv. Defines the python version, dependencies,
scripts, package indexes, etc
- **Pipfile.lock**: Lock file containing all the dependencies and installed versions.

### Commands
- `pipenv install`: Installs the runtime dependencies for the project
- `pipenv install -d`: Installs the runtime and development dependencies for the project
- `pipenv install requests`: Installs the requests package as a runtime dependency
- `pipenv install pytest -d`: Installs the pytest package as a development dependency
- `pipenv clean`: Uninstalls all packages not specified in Pipfile.lock.
- `pipenv run command`: Runs a command(or defined script) inside the virtualenv
- `pipenv shell`: Spawns a shell within the virtualenv
- `pipenv uninstall requests`: Uninstalls the requests package and removes it from the Pipfile

### Documentation
Pipenv's documentation is located [here](https://docs.pipenv.org/)