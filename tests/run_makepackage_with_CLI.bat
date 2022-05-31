:: Creating pkgCLI package with CLI
CALL makepackage pkgCLI cli

:: Deactivating the makepackage venv
CALL deactivate

:: Creating and activating a new venv, venv-pkgCLI
CALL python -m venv venv-pkgCLI
CALL .\venv-pkgCLI\Scripts\activate

:: Installing the package in editable and development mode
cd pkgCLI
CALL python -m pip install -e .[dev]

:: Running pytests of pkgCLI
CALL python -m pytest

:: Running doctests of pkgCLI - no output expected
CALL python -m doctest pkgCLI\pkgCLI.py

:: Running package as a CLI command
CALL pkgCLI

:: Deactivating the pkgCLI venv
CALL deactivate

cd ..
