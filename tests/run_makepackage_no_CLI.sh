# Run the script in a venv with makepackage installed.

echo Creating pkg package
makepackage pkg

echo Deactivating the makepackage venv
deactivate

echo
echo Creating and activating a new venv, venv-pkg
python -m venv venv-pkg
source venv-pkg/bin/activate

echo
echo Installing the package in editable and development mode
cd pkg
python -m pip install -e .[dev]

echo
echo Running pytests of pkg
pytest

echo Running doctests of pkg - no output expected
python -m doctest pkg/pkg.py

echo Deactivating venv-pkg
deactivate

cd ..
