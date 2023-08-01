import platform
from typing import Dict, List

import pytest


@pytest.fixture
def py_cmd() -> str:
    return "python" if platform.system() == "Windows" else "python3"


@pytest.fixture
def files_no_CLI() -> Dict[str, List[str]]:
    return {
        "root": [
            "README.md",
            ".gitignore",
            "pytest.ini",
            "setup.py",
            "LICENSE",
        ],
        "src": ["__init__.py", "pkgNoCLI.py"],
        "test": ["__init__.py", "conftest.py", "test_pkgNoCLI.py"],
    }


@pytest.fixture
def files_with_CLI() -> Dict[str, List[str]]:
    return {
        "root": [
            "README.md",
            ".gitignore",
            "pytest.ini",
            "setup.py",
            "LICENSE",
        ],
        "src": ["__init__.py", "__main__.py", "pkgWithCLI.py"],
        "test": ["__init__.py", "conftest.py", "test_pkgWithCLI.py"],
    }
