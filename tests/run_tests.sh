# These tests assume that you have a venv-makepackage virtual environment
# installed two folders above (../../venv-makepackage).
# Run the script in a venv with makepackage installed.

source ../../venv-makepackage/bin/activate
source run_makepackage_no_CLI.sh
source ../../venv-makepackage/bin/activate
source run_makepackage_with_CLI.sh

# The actual testing of makepackage.
# Interestingly, as the dev mode of the pkg and pkgCLI packages
# include pytest, we can run pytest inside venv-pkg
# Note also that pytest would catch also pkg's (pkgCLI's) tests,
# so we will run the test_makepackage.py test directly.
# The tests will remove pkg- and pkgCLI-related folders
source ../../venv-makepackage/bin/activate
echo Running pytests of makepackage
cd ..
pytest tests/test_makepackage.py
cd tests
