import platform
import subprocess
from pathlib import Path
from typing import Any, Dict, List

import pytest


def assert_sys(linux_condition: Any, windows_condition: Any) -> Any:
    """Assert a condition based on the operating system.

    Args:
        linux_condition (bool): condition to be checked in Linux
        windows_condition (bool): condition to be checked in Windows
    """
    if platform.system() == "Linux":
        assert linux_condition
    else:
        assert windows_condition


def choose_object_for_sys(linux_object: Any, windows_object: Any) -> Any:
    """Assign an object based on the operating system.

    Args:
        linux_object (any): object to be returned in Linux
        windows_object (bool): object to be returned in Windows
    """
    if platform.system() == "Linux":
        return linux_object
    else:
        return windows_object


# def test_folders_no_CLI(testing_path: Path):
#     assert_sys(
#         (testing_path / "venv-pkgNoCLI").exists(),
#         (testing_path / "venv-pkgNoCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgNoCLI").exists(),
#         (testing_path / "pkgNoCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgNoCLI" / "pkgNoCLI").exists(),
#         (testing_path / "pkgNoCLIWin" / "pkgNoCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgNoCLI" / "tests").exists(),
#         (testing_path / "pkgNoCLIWin" / "tests").exists(),
#     )


# def test_folders_with_CLI(testing_path: Path):
#     assert_sys(
#         (testing_path / "venv-pkgWithCLI").exists(),
#         (testing_path / "venv-pkgWithCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgWithCLI").exists(),
#         (testing_path / "pkgWithCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgWithCLI" / "pkgWithCLI").exists(),
#         (testing_path / "pkgWithCLIWin" / "pkgWithCLIWin").exists(),
#     )
#     assert_sys(
#         (testing_path / "pkgWithCLI" / "tests").exists(),
#         (testing_path / "pkgWithCLIWin" / "tests").exists(),
#     )


# def test_pkg_files_no_CLI(testing_path: Path, files_no_CLI: Dict[str, List[str]]):
#     root_dir = choose_object_for_sys(
#         testing_path / "pkgNoCLI", testing_path / "pkgNoCLIWin"
#     )
#     src_dir = choose_object_for_sys(root_dir / "pkgNoCLI", root_dir / "pkgNoCLIWin")
#     tests_dir = root_dir / "tests"

#     files = files_no_CLI
#     assert all((root_dir / file).exists() for file in files["root"])
#     assert all((src_dir / file).exists() for file in files["src"])
#     assert all((tests_dir / file).exists() for file in files["test"])


# def test_pkg_files_with_CLI(testing_path: Path, files_with_CLI: Dict[str, List[str]]):
#     root_dir = choose_object_for_sys(
#         testing_path / "pkgWithCLI", testing_path / "pkgWithCLIWin"
#     )
#     src_dir = choose_object_for_sys(root_dir / "pkgWithCLI", root_dir / "pkgWithCLIWin")
#     tests_dir = root_dir / "tests"

#     files = files_with_CLI

#     assert all((root_dir / file).exists() for file in files["root"])
#     assert all((src_dir / file).exists() for file in files["src"])
#     assert all((tests_dir / file).exists() for file in files["test"])


##### NEW TESTING FRAMEWORK


def test_pkg_folders_no_CLI(tmp_path: Path):
    test_dir = tmp_path / "tests"
    test_dir.mkdir()

    if platform.system() == "Windows":
        PY = "python"
    else:
        PY = "python3"

    subprocess.run(f"{PY} -m venv venv-pkgNoCLI", shell=True, cwd=test_dir)
    subprocess.run(f"makepackage pkgNoCLI", shell=True, cwd=test_dir)

    assert (test_dir / "venv-pkgNoCLI").exists()
    assert (test_dir / "pkgNoCLI").exists()
    assert (test_dir / "pkgNoCLI" / "pkgNoCLI").exists()
    assert (test_dir / "pkgNoCLI" / "tests").exists()
