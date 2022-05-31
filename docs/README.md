# Guide to create your Python package using this template

*Remove or relocate this file, so that this file is not part of the package.*

# Why

* In the final application, you can simply `import mypackage` and you have access to all the functions; since the package has its in-built testing, you can use it safely.
* To install the package, you need only one file (the .whl file created during building the package).

## Organization

This template uses the following organization of files and folders (largely based on [Python packaging](https://packaging.python.org/)). They suggest the following organization; for simplicity, we are using the `shoutpython` - you will need to change this name with the name of your choice.

```text
shoutpython
 |  README.md
 |  LICENSE
 |  setup.py
 |  pytest.ini
 |--shoutpython
 |  |  shoutpython.py
 |  |  __init__.py
 |--tests
 |  |  test_shoutpython.py
 |--docs

```

## License

And that's it. The LICENSE file can contain any common license (like MIT). If the package is to be used only internally, in a specific enterprise, you can use the following sentence: "The package is dedicated to internal use in {COMPANY_NAME}", or whatever you need to write there.

## README file

README can be written as a markdown file (as here), but also other file formats are acceptable, including .txt and .rst. Here, we assume markdown, since its syntax is slightly simpler than that of .rst files, and which offers much more than regular text files do.

## Code: `shoutpython` directory

The shoutpython/ subdirectory contains the main module, shoutpython.py. Your package can contain only one module, but also more of them, also collected in additional subdirectories, depending on the complexity of the project.

The __init__.py file remains as is, that is, empty.

## Testing

The tests folder contains tests, here collected in one test file. When you're using pytest (as here), you need a configuration file pytest.ini; you do not need to change the file that comes with the template. Remember about installing pytest in the virtual environment.

## Docs

You can store additional documentation in the docs/ folder. If you want to include doctest files, this folder offers a good place for them.

## Development

To develop, install the package as follows. First, create a virtual environment (after moving to the folder you want to create your package in):

```shell
> python3 -m venv shoutpython-venv
> shoutpython-venv/bin/activate
```

Now go to the folder, where you forked the shoutpython repository, so

```shell
(shoutpython-venv) > cd shoutpython
```

and install the package in an editable mode:

```shell
(shoutpython-venv) > pip install -e .
```

Everything is set up and you can develop the package. Remember to change several things:

* In setup.py:
 * package name
 * author(s)
 * email
 * short description
 * license
 * url
* In folder/file organization
 * the name of the folder with module(s)
 * the name of the module
 * the name of the file test, and the name of the module in this file


## Testing

Running the tests requires to run the following command in the root folder (of course in the virtual environment):

```shell
(shoutpython-venv) > pytest
```

If you use doctests in your docstrings, you can run them using the following command (in the root folder):

```shell
(shoutpython-venv) > python -m doctest shoutpython/shoutpython.py
```

In a similar way, you can run doctests in doctest files located in the doctest folder.

## Versioning

Remember to update package version once a change is made to the package and the new version is pushed to the repository.

## How to build a Python package?

To build the package, you need to go to the root folder of the package and run the following command:

```shell
(shoutpython-venv) > python setup.py sdist bdist_wheel
```

The built package is now located in the dist/ folder.

## Publishing your package in PyPi

If you want to publish it to [PyPi](https://pypi.org/), you need to install [twine](https://twine.readthedocs.io/en/latest/):

```shell
(shoutpython-venv) > python -m pip install twine
```

and run the following command (also in the package's root folder):

```shell
(shoutpython-venv) > twine upload dist/*
```

Nonetheless, if you first want to check what it will look like in PyPi, you can first upload the package to [a test version of PyPi](https://test.pypi.org/), that is, 

```shell
twine upload -r testpypi dist/*
```

Check if everything is fine, and if so, you're ready to publish the package to PyPi.

## Installation

### Installation from PyPi

If the package is in PyPi, you can install it from there like any other Python package, that is,

```shell
pip install shoutpython
```

## How to install a Python package from a wheel file?

If the package is a company's property, you will unlikely publish it to the public Python Package Index. You can distribute the package within the company using one file only, a .whl file located in the dist/ folder.

In order to do so, Save it in your project, activate the virtual environment (say, `my_app-venv`), and run the following command (in the root folder of your project):

```shell
(my_app-venv) pip install checkit --no-index --find-links file:./
```

If the .whl file of your package is located elsewhere, instead of `.` give the path to this location. The package is now installed in your virtual environment, and so you can import it in a simple way

```python
import shoutpython
```
