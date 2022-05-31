import pathlib


def write_README(path: pathlib.Path, package_name: str, CLI: bool) -> None:
    README = f"""# `{package_name}`: A Python package for ...


# Installation - development

Create a virtual environment, for example using `venv`:

```shell
$ python -m venv venv-{package_name}
$ source venv-{package_name}/bin/activate
$ mkdir {package_name}
$ cd {package_name}
$ python -m pip install -e .[dev]

```

Note that the last command installs a development environment, as it also installs packages needed for development, like `black` (for code formatting), `pytest` (for unit testing) and `wheel` (for creating wheel files from the package).
"""
    if CLI:
        README += f"""

# CLI app

`{package_name}` offers a command-line interface, which you can run from shell using the following command:

```shell
$ {package_name}
```
"""

    with open(path / "README.md", "w") as f:
        f.write(README)
