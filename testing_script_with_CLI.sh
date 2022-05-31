# Remember to run the script in a venv with makepackage installed.

cd ../dir_for_testing

echo
echo creating pkgCLI package with CLI
makepackage pkgCLI cli

echo
echo Creating a new venv, venv-pkgCLI
deactivate
python -m venv venv-pkgCLI

echo Now activating it
source venv-pkgCLI/bin/activate

echo
echo Install the package in editable mode
cd pkgCLI
python -m pip install -e .[dev]

echo
echo Running pytests
pytest

echo
echo Running doctests
python -m doctest pkgCLI/pkgCLI.py

echo
echo Running package as a CLI command
pkgCLI

cd ../../makepackage/

deactivate
source ../venv-makepackage/bin/activate
