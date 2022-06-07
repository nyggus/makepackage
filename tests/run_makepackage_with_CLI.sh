echo Creating pkgWithCLI package with CLI
makepackage pkgWithCLI cli

echo Deactivating the makepackage venv
deactivate

echo Creating and activating a new venv, venv-pkgWithCLI
python -m venv venv-pkgWithCLI
source venv-pkgWithCLI/bin/activate

echo
echo Installing the package in editable and development mode
cd pkgWithCLI
python -m pip install -e .[dev]

echo
echo Running pytests of pkgWithCLI
pytest

echo
echo Running doctests of pkgWithCLI - no output expected
python -m doctest pkgWithCLI/pkgWithCLI.py

echo
echo Running package as a CLI command
pkgWithCLI

cd ../

echo
echo Deactivating venv-pkgWithCLI
deactivate
