:: These tests assume that you have a venv-makepackage-win virtual environment
:: installed two folders above (../../venv-makepackage-win).

:: Run the script in a venv with makepackage installed.

CALL run_makepackage_no_CLI.bat
CALL ..\..\venv-makepackage-win\Scripts\activate
CALL run_makepackage_with_CLI.bat

:: The actual testing of makepackage.
:: Interestingly, as the dev mode of the pkg and pkgCLI packages
:: include pytest, we can run pytest inside venv-pkg
:: Note also that pytest would catch also pkg's (pkgCLI's) tests,
:: so we will run the test_makepackage.py test directly.
:: The tests will remove pkg- and pkgCLI-related folders
cd ..
CALL ..\venv-makepackage-win\Scripts\activate
CALL pytest tests\test_makepackage.py
