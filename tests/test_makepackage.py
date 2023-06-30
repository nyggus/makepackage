import subprocess
import platform
from pathlib import Path
from typing import Dict, List, Tuple

import pytest


def select_venv_cmd():
    if platform.system() == "Windows":
        return ".\\.venv\\Scripts\\activate"

    return "source .venv/bin/activate"


def run_cmds(cmds: List[Tuple]):
    for cmd, path in cmds:
        if platform.system() == "Windows":
            subprocess.run(cmd, shell=True, cwd=path, check=True)
        else:
            subprocess.run(
                cmd, executable="/bin/bash", shell=True, cwd=path, check=True
            )


def test_pkg_no_CLI(tmp_path: Path, py_cmd: str, files_no_CLI: Dict[str, List[str]]):
    pkg_name = "pkgNoCLI"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"
    venv_command = select_venv_cmd()

    commands = [
        (f"makepackage {pkg_name}", tmp_path),
        (f"{py_cmd} -m venv .venv && {venv_command} && pip install -e .", pkg_path),
        ("pytest", pkg_path),
        (f"{py_cmd} -m doctest {src_dir / pkg_name}.py", pkg_path),
    ]

    run_cmds(commands)

    files = files_no_CLI

    assert (pkg_path / ".venv").exists()
    assert (pkg_path).exists()
    assert (src_dir).exists()
    assert (tests_dir).exists()

    assert all((pkg_path / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])


def test_pkg_with_CLI(
    tmp_path: Path,
    py_cmd: str,
    files_with_CLI: Dict[str, List[str]],
):
    pkg_name = "pkgWithCLI"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"
    venv_command = select_venv_cmd()

    commands = [
        (f"makepackage {pkg_name} --cli", tmp_path),
        (f"{py_cmd} -m venv .venv && {venv_command} && pip install -e .", pkg_path),
        ("pytest", pkg_path),
        (f"{py_cmd} -m doctest {src_dir / pkg_name}.py", pkg_path),
    ]

    run_cmds(commands)

    files = files_with_CLI

    assert (pkg_path / ".venv").exists()
    assert (pkg_path).exists()
    assert (src_dir).exists()
    assert (tests_dir).exists()

    assert all((pkg_path / file).exists() for file in files["root"])
    assert all((src_dir / file).exists() for file in files["src"])
    assert all((tests_dir / file).exists() for file in files["test"])
