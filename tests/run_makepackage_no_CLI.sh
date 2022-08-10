# Run the script in a venv with makepackage installed.

echo Creating pkgNoCLI package
makepackage pkgNoCLI

echo Deactivating the makepackage venv
deactivate

echo
echo Creating and activating a new venv, venv-pkgNoCLI
python -m venv venv-pkgNoCLI
source venv-pkgNoCLI/bin/activate

echo
echo Installing the package in editable and development mode
cd pkgNoCLI
python -m pip install -e .[dev]

echo
echo Running pytests of pkgNoCLI
pytest

echo Running doctests of pkgNoCLI - no output expected
python -m doctest pkgNoCLI/pkgNoCLI.py

echo Deactivating venv-pkgNoCLI
deactivate

cd ..
