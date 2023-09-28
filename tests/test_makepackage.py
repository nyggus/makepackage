from __future__ import annotations

import platform
import subprocess
from pathlib import Path
from typing import Tuple

cmd_command = Tuple[str, Path]


def select_venv_cmd():
    if platform.system() == "Windows":
        return r".\.venv\Scripts\activate"

    return "source .venv/bin/activate"


def run_cmds(cmds: list[cmd_command]):
    if platform.system() == "Windows":
        executable = None
    else:
        executable = "/bin/bash"

    for cmd, path in cmds:
        process = subprocess.Popen(
            args=cmd,
            shell=True,
            executable=executable,
            cwd=path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        _, stderr = process.communicate()

        if process.returncode != 0:
            raise RuntimeError(
                f"Command failed with error code {process.returncode}: {stderr.decode()}"
            )


def test_pkg_no_CLI(tmp_path: Path, py_cmd: str, files_no_CLI: dict[str, list[str]]):
    pkg_name = "pkgNoCLI"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"
    venv_command = select_venv_cmd()

    commands = [
        (f"makepackage {pkg_name}", tmp_path),
        (
            f"{py_cmd} -m venv .venv && {venv_command} && pip install -e .",
            pkg_path,
        ),
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
    files_with_CLI: dict[str, list[str]],
):
    pkg_name = "pkgWithCLI"
    pkg_path = tmp_path / pkg_name
    src_dir = tmp_path / pkg_name / pkg_name
    tests_dir = tmp_path / pkg_name / "tests"
    venv_command = select_venv_cmd()

    commands = [
        (f"makepackage {pkg_name} --cli", tmp_path),
        (
            f"{py_cmd} -m venv .venv && {venv_command} && pip install -e .",
            pkg_path,
        ),
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
