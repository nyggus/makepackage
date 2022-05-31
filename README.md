# `makepackage`: A Python package for creating a Python package with a simple structure

## Rationale

You may know the story. For over a year, I have been developing most of my projects as Python packages. I created a template, as doing the same thing manually every time was boring and slow. But such a template required much manual work, and every time I made some mistakes so that I had to look for them and fix.

Then I thought that a script will be betterm so I wrote one. It worked fine indeed, and it was practically error-free. And then I thought, as this is so useful for me, why not make it useful for others? So, I made this package, and now you can use it just like me.

The only thing you need to do is to install `makepackage` and run a simple shell command - that's all you need!


## Background and purpose

Many projects are designed as Python packages. Such an approach has lots of advantages, but creating such a package does not have to be straightforward. You can use tools such as [Cookiecutter](https://cookiecutter.readthedocs.io/), but they themselves are quite advanced and offer a lot of functionalities that you need to learn.

The `makepackage` Python package offers a lightweight alternative for creating a Python package. It offers only one function that is run from shell (under both Linux and Windows), and it creates a Python package with only two possibilities: with or without command-line interface.

The use of `makepackage` is very simple, but this does not come without costs: it creates just one type of structure, though you can change it manually:
* you have to fill in some fields in setup.py
* setup.py will include `pytest`, `wheel` and `black` in the `dev` mode; you can remove them manually before installation
* the package uses `pytest` and `doctest`

The idea behind `makepackage` is to offer a tool that creates a working simplistic package that one can extend and develop. And indeed, you will find in it tests that pass (both `pytest` and `doctest`); you can install the package in the editable mode, and after that you will be able to import it. So, the resulting package is just fine, and you can immediately move to development.


> `makepackage` offers one many possible structures, and it assumes you will use `pytest` for testing. If you want to use other solutions,  you should either create a package manually or use another tool.


## Using `makepackage`

> The [tests](tests/) folder contains six shell scripts. Two of them show how to use `makepackage` in Linux, and two others do the same for Windows. One of the scripts shows how to create a package that does not need command-line interface while the other with CLI. Check out these two files for Linux: [`makepackage` without CLI](tests/run_makepackage_no_CLI.sh) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.sh); and for Windows, these two files: [`makepackage` without CLI](tests/run_makepackage_no_CLI.bat) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.bat).

It's best to install and use `makepackage` through a virtual environment. So, for example,

```shell
$ python -m venv venv-makepackage
$ venv-package/bin/activate
(venv-makepackage) $ pip install makepackage
```

> Examples show Linux commands, but any Windows user will know how to replace them with the corresponding Windows commands (though most commands will be the same in Linux and Windows).

Now that we have activated the virtual environment and installed `makepackage` in it, we are ready to create a package of our own. First, navigate to a folder where you want to create the package, and run the following command:

```shell
(venv-makepackage) $ makepackage ziuziu
```

This creates a `ziuziu` package; `ziuziu` will not have command-line interface. You will now see a ziuziu folder:

```shell
(venv-makepackage) $ ls
ziuziu
```

If you want to create a package with command-line interface, use a command-line argument `cli`, like this:

```shell
(venv-makepackage) $ makepackage ziuziu cli
```

With this, you will be able to run your package using the `ziuziu` command in shell.

The only thing you now need to do is to create a virtual environment and install the `ziuziu` package there, in the editable mode:

```shell
(venv-package) $ deactivate
$ python -m pip install venv-ziuziu
(venv-ziuziu) $ cd ziuziu
(venv-ziuziu) $ python -m pip install -e .[dev]
```

And that's it, you're ready to develop `ziuziu`. Now you can run tests:

```shell
(venv-ziuziu) $ python -m pytest
```

You will see that the package is created with 11 `pytest` tests, and they should all pass (you will see the output from `pytest`).


> When you create a package using `makepackage`, you can read the README file of the new package. It contains some essential information about package development, such as buidling the package, installing it, and uploading to PyPi.

## Structure of a package created using `makepackage`

You can use various structures to create a Python package. `makepackage` uses one of them, a simple (though not the simplest) one. You will see the following structure of the ziuziu/ folder (so, of the `ziuziu` package):

```shell
.
+-- README.md
+-- .gitignore
+-- LICENSE
+-- setup.py
+-- pytest.ini
+-- ziuziu/
|  +-- ziuziu.py/
|  +-- __init__.py
+-- tests
|  +-- __init__.py
|  +-- conftest.py
|  +-- test_ziuziu.py

```

When you used the `makepackage` command with the `cli` argument, the `ziuziu/ziuziu` folder will also inlcude a `__main__.py` file.

Here are the assumptions `makepackage` makes:
* the package is developed using `pytest` and `doctest` (you will find both implemented in the code of `ziuziu`)
* MIT license is used (you can change it to any license you want, but remember also to change the license in setup.py)
* in the development mode, `pytest`, `wheel` and `black` packages are additionally installed in the virtual environment (used for development)
* you will need to fill setup.py in several places (namely, fields `author`, `author_email`, and `description`) and LICENSE in one place; you can easily find those places, as they are indicated with the `"[MAKEPACKAGE]"` mark

Of course, this is a starting point, and you can now extend the package however you want. Once installed, `ziuziu` (or however you name the package) works. It has three functions, `foo()`, `bar()` and `baz()`, which all have tests implemented in the tests/ folder, and you can run them using the `pytest` command.

Those who tried to create such a package manually know that quite often something does not work - an import does not work, `pytest` does not see the package, and the like. When using `makepackage`, you get a fully working structure of the package. The only thing you need to do is to replace the existing functions with your functions, and of course to adapt the package to this change (in __init__.py, tests/ etc.).


> `makepackage` comes with some functionalities that you can get rid of:
>> A conftest.py file in the tests/ folder.
>> Simple annotations in the `foo()`, `bar()` and `baz()` functions of the newly created package.
>> Each function has a simple docstring with doctests.


# Notes on further development

As mentioned before, the first step is to fill in several fields in setup.py and author in LICENSE. Then you need to create a virtual environment, in which you install the package in the editable mode. And that's all you need to start development. 

From now on, you're on your own. However, a package created using `makepackage` comes with some help for inexperienced users. They can see how to write tests (using `pytest`), how to use a conftest.py file (for `pytest`ing), how to write fixtures and use parametrized tests (again for `pytest`ing), how to import the package's modules and functions, and the like. These are just some basic development tools. 

There is one thing I'd like to stress, and it's related to imports (actually, imports often pose some strange problems during Python development). When you add a new module to the source folder (in our example, this is ziuziu/), e.g., ziuziu/another_ziuziu.py, then in the main `ziuziu` module you can import it as `from ziuziu import another_ziuziu` or `from ziuziu.another_ziuziu import another_foo`. Note that the regular approach you would use, that is, `import another_ziuziu`, will not work here.


## Testing

Testing of `makepackage` combines shell scripts and `pytest`. Therefore, running tests on Linux and Windows requires running different shell scripts. You will learn more from [here](tests/README.md).
