import configparser
from pathlib import Path


def write_pyproject(path: Path, package_name: str, CLI: bool) -> None:
    config = configparser.ConfigParser()

    # Add sections to the ConfigParser object
    config["build-system"] = {
        "requires": ["setuptools>=61.0"],
        "build-backend": '"setuptools.build_meta"',
    }
    config["project"] = {
        "name": f"'{package_name}'",
        "version": '"0.1.0"',
        "authors": {"name": "[MAKEPACKAGE]", "email": "[MAKEPACKAGE]"},
        "description": '"[MAKEPACKAGE]"',
        "readme": '"README.md"',
        "license": {"file": "LICENSE"},
        "requires-python": '">=3.8"',
        "dependencies": ["easycheck"],
        "classifiers": [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    }
    config["project.urls"] = {"Homepage": '"[MAKEPACKAGE]"'}
    config["tool.setuptools"] = {"packages": [f"{package_name}"]}

    if CLI:
        config["project.scripts"] = {f"{package_name}": f'"{package_name}.__main__:main"'}

    config["project.optional-dependencies"] = {
        "dev": ["wheel", "black", "pytest", "mypy"]
    }

    with open(path / "pyproject.toml", "w") as f:
        config.write(f)
