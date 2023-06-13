import platform
import subprocess
from pathlib import Path
from typing import Dict, List

import pytest


def test_pkg_no_CLI(tmp_path: Path, files_no_CLI: Dict[str, List[str]]):
    PY_CMD = "python" if platform.system() == "Windows" else "python3"
    pkg_name = "pkgNoCLI"
    venv = f"venv-{pkg_name}"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"

    subprocess.run(f"{PY_CMD} -m venv {venv}", shell=True, cwd=tmp_path)
    subprocess.run(f"makepackage {pkg_name}", shell=True, cwd=tmp_path)
    subprocess.run(f"{PY_CMD} -m pip install -e .", shell=True, cwd=pkg_path)
    subprocess.run("pytest", shell=True, cwd=pkg_path)
    subprocess.run(
        f"{PY_CMD} -m doctest {src_dir / pkg_name}.py", shell=True, cwd=pkg_path
    )

    files = files_no_CLI

    assert (tmp_path / venv).exists()
    assert (pkg_path).exists()
    assert (src_dir).exists()
    assert (tests_dir).exists()

    assert all((pkg_path / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])


def test_pkg_with_CLI(tmp_path: Path, files_with_CLI: Dict[str, List[str]]):
    PY_CMD = "python" if platform.system() == "Windows" else "python3"
    pkg_name = "pkgWithCLI"
    venv = f"venv-{pkg_name}"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"

    subprocess.run(f"{PY_CMD} -m venv {venv}", shell=True, cwd=tmp_path)
    subprocess.run(f"makepackage {pkg_name} --cli", shell=True, cwd=tmp_path)
    subprocess.run(f"{PY_CMD} -m pip install -e .", shell=True, cwd=pkg_path)
    subprocess.run("pytest", shell=True, cwd=pkg_path)
    subprocess.run(
        f"{PY_CMD} -m doctest {src_dir / pkg_name}.py", shell=True, cwd=pkg_path
    )

    files = files_with_CLI

    assert (tmp_path / venv).exists()
    assert (pkg_path).exists()
    assert (src_dir).exists()
    assert (tests_dir).exists()

    assert all((pkg_path / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])
