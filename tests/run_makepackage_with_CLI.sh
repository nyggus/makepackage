echo Creating pkgCLI package with CLI
makepackage pkgCLI cli

echo Deactivating the makepackage venv
deactivate

echo Creating and activating a new venv, venv-pkgCLI
python -m venv venv-pkgCLI
source venv-pkgCLI/bin/activate

echo
echo Installing the package in editable and development mode
cd pkgCLI
python -m pip install -e .[dev]

echo
echo Running pytests of pkgCLI
pytest

echo
echo Running doctests of pkgCLI - no output expected
python -m doctest pkgCLI/pkgCLI.py

echo
echo Running package as a CLI command
pkgCLI

cd ../

echo
echo Deactivating venv-pkgCLI
deactivate
