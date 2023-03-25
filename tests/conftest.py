import pathlib
import platform
import pytest
import shutil

from typing import Dict, Iterator, List


@pytest.fixture
def testing_path() -> pathlib.Path:
    return pathlib.Path(".") / "tests"


@pytest.fixture
def files_no_CLI() -> Iterator[Dict[str, List[str]]]:
    if platform.system() == "Linux":
        yield {
            "root": [
                "README.md",
                ".gitignore",
                "pytest.ini",
                "setup.cfg",
                "pyproject.toml",
                "LICENSE",
            ],
            "src": ["__init__.py", "pkgNoCLI.py"],
            "test": ["__init__.py", "conftest.py", "test_pkgNoCLI.py"],
        }
    else:
        yield {
            "root": [
                "README.md",
                ".gitignore",
                "pytest.ini",
                "setup.cfg",
                "pyproject.toml",
                "LICENSE",
            ],
            "src": ["__init__.py", "pkgNoCLIWin.py"],
            "test": ["__init__.py", "conftest.py", "test_pkgNoCLIWin.py"],
        }


@pytest.fixture
def files_with_CLI() -> Iterator[Dict[str, List[str]]]:
    if platform.system() == "Linux":
        yield {
            "root": [
                "README.md",
                ".gitignore",
                "pytest.ini",
                "setup.cfg",
                "pyproject.toml",
                "LICENSE",
            ],
            "src": ["__init__.py", "__main__.py", "pkgWithCLI.py"],
            "test": ["__init__.py", "conftest.py", "test_pkgWithCLI.py"],
        }
    else:
        yield {
            "root": [
                "README.md",
                ".gitignore",
                "pytest.ini",
                "setup.cfg",
                "pyproject.toml",
                "LICENSE",
            ],
            "src": ["__init__.py", "__main__.py", "pkgWithCLIWin.py"],
            "test": ["__init__.py", "conftest.py", "test_pkgWithCLIWin.py"],
        }

    # Cleanup
    for dir in (
        "pkgNoCLI",
        "venv-pkgNoCLI",
        "pkgWithCLI",
        "venv-pkgWithCLI",
        "pkgNoCLIWin",
        "venv-pkgNoCLIWin",
        "pkgWithCLIWin",
        "venv-pkgWithCLIWin",
    ):
        shutil.rmtree(pathlib.Path("tests") / dir, ignore_errors=True)
