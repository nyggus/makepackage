:: Creating pkgCLI package with CLI
CALL makepackage pkgWithCLIWin cli

:: Deactivating the makepackage venv
CALL deactivate

:: Creating and activating a new venv, venv-pkgCLI
CALL python -m venv venv-pkgWithCLIWin
CALL .\venv-pkgWithCLIWin\Scripts\activate

:: Installing the package in editable and development mode
cd pkgWithCLIWin
CALL python -m pip install -e .[dev]

:: Running pytests of pkgCLI
CALL python -m pytest

:: Running doctests of pkgCLI - no output expected
CALL python -m doctest pkgWithCLIWin\pkgWithCLIWin.py

:: Running package as a CLI command
CALL pkgWithCLIWin

:: Deactivating the pkgCLI venv
CALL deactivate

cd ..
