import pathlib
import pytest
import shutil


@pytest.fixture
def testing_path():
    return pathlib.Path(".") / "tests"


@pytest.fixture
def files_no_CLI():
    yield {
        "root": [
            "README.md",
            ".gitignore",
            "pytest.ini",
            "setup.py",
            "LICENSE",
        ],
        "src": ["__init__.py", "pkg.py"],
        "test": ["__init__.py", "conftest.py", "test_pkg.py"],
    }


@pytest.fixture
def files_with_CLI():
    yield {
        "root": [
            "README.md",
            ".gitignore",
            "pytest.ini",
            "setup.py",
            "LICENSE",
        ],
        "src": ["__init__.py", "__main__.py", "pkgCLI.py"],
        "test": ["__init__.py", "conftest.py", "test_pkgCLI.py"],
    }

    # Cleanup
    for dir in ("pkg", "venv-pkg", "pkgCLI", "venv-pkgCLI"):
        shutil.rmtree(pathlib.Path("tests") / dir)
