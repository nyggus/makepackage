import sys
from collections import namedtuple
from easycheck import check_length, gt, lt
from makepackage import (
    NoPackageNameError,
    IncorrectCLIArgumentError,
    makepackage,
)


def main():
    package_name, CLI = _read_cli_args()
    makepackage(package_name, CLI)
    print_final_info


def _read_cli_args():
    check_length(
        sys.argv,
        1,
        NoPackageNameError,
        operator=gt,
        message="Provide package name as the first CLI argument",
    )
    check_length(
        sys.argv,
        4,
        IncorrectCLIArgumentError,
        operator=lt,
        message="Expected two CLI args: package name and (optionally) CLI",
    )
    package_name = sys.argv[1]
    try:
        CLI = True if sys.argv[2].lower() == "cli" else False
    except IndexError:
        CLI = False
    print(
        f"Creating package <{package_name}>, "
        f"with{'' if CLI else 'out'} command-line interface."
    )
    return namedtuple("Settings", "package_name CLI")(package_name, CLI)


def print_final_info(package_name: str) -> None:
    print(
        f"Package <{package_name}> has been created.\n"
        "Check out above if all the tests (both pytests and doctests) have passed - they should."
        "To finish, you need to fill in the following fields in setup.py:\n"
        "  - author\n"
        "  - author_email\n"
        "  - description (this is a short description, as the long one is taken from README)\n"
        "You need to also fill in the author in LICENSE. You can find all those fields"
        "by searching for '[MAKEPACKAGE]' in the project.\n"
        "When you're done, the package is ready to be develop.\n"
        "Check if you need all libraries from extras_require in setup.py - they will "
        "be installed in the development mode of the package (not after installing from "
        "the wheel file)."
    )


if __name__ == "__main__":
    main()
