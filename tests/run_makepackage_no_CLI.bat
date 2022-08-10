:: Run the script in a venv with makepackage installed.

:: Creating pkg package
CALL makepackage pkgNoCLIWin

:: Deactivating the makepackage venv
CALL deactivate

:: Creating and activating a new venv, venv-pkg
CALL python -m venv venv-pkgNoCLIWin
CALL .\venv-pkgNoCLIWin\Scripts\activate.bat

:: Installing the package in editable and development mode
cd pkgNoCLIWin
CALL python -m pip install -e .[dev]

:: Running pytests of pkg
CALL python -m pytest

:: Running doctests of pkg - no output expected
CALL python -m doctest pkgNoCLIWin\pkgNoCLIWin.py

:: Deactivating the pkg venv
CALL deactivate

cd ..
