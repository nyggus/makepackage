# Remember to run the script in a venv with makepackage installed.

cd ../dir_for_testing

echo
echo creating pkg package
makepackage pkg

echo
echo Creating a new venv, venv-pkg
deactivate
python -m venv venv-pkg

echo Now activating it
source venv-pkg/bin/activate

echo
echo Install the package in editable mode
cd pkg
python -m pip install -e .[dev]

echo
echo Running pytests
pytest

echo
echo Running doctests
python -m doctest pkg/pkg.py

cd ../../makepackage/

deactivate
source ../venv-makepackage/bin/activate
