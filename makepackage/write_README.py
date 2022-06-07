from pathlib import Path


def write_README(path: Path, package_name: str, CLI: bool) -> None:
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


# Testing

Running the tests requires to run the following command in the root folder (of course in the virtual environment):

```shell
(venv-{package_name}) > pytest
```

If you use doctests in your docstrings (as `makepackage` assumes), you can run them using the following command (in the root folder):

```shell
(venv-{package_name}) > python -m doctest {package_name}/{package_name}.py
```

In a similar way, you can run doctests from any other file that contains doctests.


## Versioning

Remember to update package version once a change is made to the package and the new version is pushed to the repository. Don't forget about releases, too.


## How to build a Python package?

To build the package, you need to go to the root folder of the package and run the following command:

```shell
(venv-{package_name}) > python setup.py sdist bdist_wheel
```

Note that this assumes you have `wheel` installed in your virtual environment, and `makepackage` does this for you.

The built package is now located in the dist/ folder.


## Publishing your package in PyPi

If you want to publish it to [PyPi](https://pypi.org/), you need to install [twine](https://twine.readthedocs.io/en/latest/), create an account there, and run the following command (also in the package's root folder):

```shell
(venv-{package_name}) > twine upload dist/*
```

Nonetheless, if you first want to check what it will look like in PyPi, you can first upload the package to [a test version of PyPi](https://test.pypi.org/), that is, 

```shell
twine upload -r testpypi dist/*
```

Check if everything is fine, and if so, you're ready to publish the package to PyPi.

## Installation from PyPi

If the package is in PyPi, you can install it from there like any other Python package, that is,

```shell
pip install 
```
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
