import os
from easycheck import check_if_not
from pathlib import Path

from makepackage.write_README import write_README
from makepackage.write_setup import write_setup
from makepackage.write_license import write_license
from makepackage.write_gitignore import write_gitignore
from makepackage.write_CLI_main import write_CLI_main

from makepackage.write_module_init import write_module_init
from makepackage.write_module import write_module

from makepackage.write_pytest_ini import write_pytest_ini
from makepackage.write_conftest import write_conftest
from makepackage.write_tests import write_tests
from makepackage.write_tests_init import write_tests_init


class NoPackageNameError(Exception):
    pass


class IncorrectCLIArgumentError(Exception):
    pass


class FolderExistsError(Exception):
    pass


def makepackage(package_name: str, CLI: bool) -> None:

    # create directories
    root_path = (Path(".") / f"{package_name}").absolute()
    make_dirs(root_path, package_name)

    # write files in the root folder
    write_setup(root_path, package_name, CLI)
    write_README(root_path, package_name, CLI)
    write_pytest_ini(root_path)
    write_license(root_path)
    write_gitignore(root_path)

    # write files in the module's folder
    module_path = root_path / f"{package_name}"
    write_module(module_path, package_name)
    write_module_init(module_path, package_name)

    # write files in the tests/ folder
    tests_path = root_path / "tests"
    write_conftest(tests_path)
    write_tests_init(tests_path)
    write_tests(tests_path, package_name)

    # write __main__, if CLI is True
    if CLI:
        write_CLI_main(module_path, package_name)


def make_dirs(root_path: Path, package_name: str) -> None:
    check_if_not(
        root_path.exists(),
        FolderExistsError,
        message=f"Folder {root_path} already exists.",
    )
    os.mkdir(str(root_path))
    for dir in {
        "tests",
        package_name,
    }:
        this_path = root_path / dir
        check_if_not(
            this_path.exists(),
            FolderExistsError,
            message=f"Folder {dir} already exists.",
        )
        os.mkdir(str(this_path))
