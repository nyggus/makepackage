import configparser
from pathlib import Path


def write_setup_cfg(path: Path, package_name: str, CLI: bool) -> None:
    config = configparser.ConfigParser()

    # Add sections to the ConfigParser object
    config["metadata"] = {
        "name": f"{package_name}",
        "version": "0.1.0",
        "author": "[MAKEPACKAGE]",
        "author_email": "[MAKEPACKAGE]",
        "description": "[MAKEPACKAGE]",
        "long_description": "file: README.md",
        "long_description_content_type": "text/markdown",
        "url": "[MAKEPACKAGE]",
        "license_files": "LICENSE",
        "classifiers": "\n".join(
            [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ]
        ),
    }

    config["options"] = {
        "packages": "\n".join([f"{package_name}"]),
        "python_requires": ">=3.6",
        "install_requires": "\n".join(["easycheck"]),
    }

    if CLI:
        config["options.entry_points"] = {
            f"{package_name}": f"{package_name}.__main__:main"
        }

    config["options.extras_require"] = {
        "dev": "\n".join(["wheel", "black", "pytest", "mypy", "build"]),
    }

    with open(path / "setup.cfg", "w") as f:
        config.write(f)
