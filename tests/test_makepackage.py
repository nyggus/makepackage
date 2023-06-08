import platform
import subprocess
from pathlib import Path
from typing import Dict, List

import pytest


def test_pkg_no_CLI(tmp_path: Path, files_no_CLI: Dict[str, List[str]]):
    PY = "python" if platform.system() == "Windows" else "python3"

    subprocess.run(f"{PY} -m venv venv-pkgNoCLI", shell=True, cwd=tmp_path)
    subprocess.run("makepackage pkgNoCLI", shell=True, cwd=tmp_path)

    files = files_no_CLI

    assert (tmp_path / "venv-pkgNoCLI").exists()
    assert (tmp_path / "pkgNoCLI").exists()
    assert (tmp_path / "pkgNoCLI" / "pkgNoCLI").exists()
    assert (tmp_path / "pkgNoCLI" / "tests").exists()

    assert all((tmp_path / "pkgNoCLI" / file).exists() for file in files["root"])
    assert all(
        (tmp_path / "pkgNoCLI" / "pkgNoCLI" / file).exists() for file in files["src"]
    )
    assert all(
        (tmp_path / "pkgNoCLI" / "tests" / file).exists() for file in files["test"]
    )


def test_pkg_with_CLI(tmp_path: Path, files_with_CLI: Dict[str, List[str]]):
    PY = "python" if platform.system() == "Windows" else "python3"

    subprocess.run(f"{PY} -m venv venv-pkgWithCLI", shell=True, cwd=tmp_path)
    subprocess.run("makepackage pkgWithCLI --cli", shell=True, cwd=tmp_path)

    files = files_with_CLI

    assert (tmp_path / "venv-pkgWithCLI").exists()
    assert (tmp_path / "pkgWithCLI").exists()
    assert (tmp_path / "pkgWithCLI" / "pkgWithCLI").exists()
    assert (tmp_path / "pkgWithCLI" / "tests").exists()

    assert all((tmp_path / "pkgWithCLI" / file).exists() for file in files["root"])
    assert all(
        (tmp_path / "pkgWithCLI" / "pkgWithCLI" / file).exists()
        for file in files["src"]
    )
    assert all(
        (tmp_path / "pkgWithCLI" / "tests" / file).exists() for file in files["test"]
    )
