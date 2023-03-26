import configparser
from pathlib import Path


def write_pyproject(path: Path, package_name: str, CLI: bool) -> None:
    config = configparser.ConfigParser()

    # Add sections to the ConfigParser object
    config["build-system"] = {
        "requires": ["setuptools>=61.0"],
        "build-backend": '"setuptools.build_meta"',
    }
