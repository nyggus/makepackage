# `makepackage`: A Python package for packaging Python code

## Rationale and background

Organizing Python code in a package has a lot of advantages and actually simplifies development — but the first hours can be tricky. To facilitate this process, you can use tools such as [Cookiecutter](https://cookiecutter.readthedocs.io/), but they themselves are quite advanced and offer a lot of functionalities that you need to learn — quite often, this complexity makes development more difficult, sometimes changing it to a nightmare. 

To facilitate this step, I created a package template and have been using it for about a year. Life got easier. But the template required some manual work that could be automated. This is when I thought that a script would be better, so I wrote one. It worked fine indeed, and things got even easier. And then I thought, as this is so useful for me, why not make it useful for others? So, I made this package, and now you can use it just like me.

`makepackage` offers only one function, available via shell. The only thing you need to do is to install `makepackage` (e.g., in a virtual environment or in your system Python installation) and run a simple shell command (which works under both Linux and Windows). The command, as you will see below, takes one required argument: a package's name; you can add `cli` to create a CLI package, as otherwise it will not have command-line interface.

The use of `makepackage` is very simple, but this does not come without costs: it creates just one type of structure, though you can change it manually:
* you have to fill in some fields in setup.py
* setup.py will include `pytest`, `wheel`, `black` and `mypy` in the `dev` mode; you can remove them manually before installation
* the package will use `pytest` for unit testing and `doctest`  for documentation testing

> You will find annotated code in `ziuziu` (given the simplicity of the functions, the annotations are very simple), and you can run `mypy` on it, with success.

The idea behind `makepackage` is to offer a tool that creates a working simplistic package that one can extend and develop. And indeed, you will find in it tests (both `pytest`s and `doctest`s) that pass; you can install the package in the editable mode, and after that you will be able to import it. So, the resulting package is just fine, and you can immediately move to development.


> `makepackage` offers one of many possible structures, and it assumes you will use `pytest` (plus, optionally, `doctest`) for testing. If you want to use other solutions,  you should either create a package manually or use another tool.


## Using `makepackage`

> The [tests](tests/) folder contains six shell scripts. Two of them show how to use `makepackage` in Linux, and two others do the same for Windows. One of the scripts shows how to create a package that does not need command-line interface while the other with CLI. Check out these two files for Linux: [`makepackage` without CLI](tests/run_makepackage_no_CLI.sh) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.sh); and for Windows, these two files: [`makepackage` without CLI](tests/run_makepackage_no_CLI.bat) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.bat).

It's best to install and use `makepackage` through a virtual environment dedicated to this package. So, for example,

```shell
$ python -m venv venv-makepackage
$ venv-package/bin/activate
(venv-makepackage) $ pip install makepackage
```

> Examples use Linux commands, but most of them will work the same way for Windows.

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

> As we used the same name — `ziuziu` — again, we would get an error; so, you should first remove the previous installation of `ziuziu`, use a different name for the package, or create the package in a different location.

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
(venv-ziuziu) $ python -m doctest ziuziu/ziuziu.py
```

You will see that the package is created with 11 `pytest` tests, and they should all pass (you will see the output from `pytest`). All `doctest`s should pass, too — that means you should see no output from `doctest`.


> When you create a package using `makepackage`, you can read the README file of the new package. It contains additional information about package development, such as buidling the package, installing it, and uploading to PyPi.

## Structure of a package created using `makepackage`

You can use various structures to create a Python package. `makepackage` uses one of them, a simple (though not the simplest) one. You will see the following structure of the ziuziu/ folder (so, of the `ziuziu` package):

```shell
.
+-- .gitignore
+-- LICENSE
+-- README.md
+-- pytest.ini
+-- setup.py
+-- tests
|  +-- __init__.py
|  +-- conftest.py
|  +-- test_ziuziu.py
+-- ziuziu/
|  +-- ziuziu.py
|  +-- __init__.py

```

When you used the `makepackage` command with the `cli` argument, the `ziuziu/ziuziu` folder will also include a `__main__.py` file.

Here are the assumptions `makepackage` makes:
* the package is developed using `pytest` and `doctest` (you will find both implemented in the code of `ziuziu`; you can easily get rid of `doctest`s, but if you've got an idea of removing `pytest`s, this means you probably should have not used `makepackage`)
* MIT license is used (you can change it to any license you want, but remember also to change the license type in setup.py)
* in the development mode, `pytest`, `wheel`, `black` and `mypy` packages are additionally installed in the virtual environment (they are used during package development and building)
* you will need to fill in setup.py in several places (namely, fields `author`, `author_email`, and `description`) and LICENSE in one place; you can easily find those places, as they are indicated with the `"[MAKEPACKAGE]"` mark

Of course, this is a starting point, and you can now extend the package however you want. Once installed, `ziuziu` (or however you name the package) works. It has three functions, `foo()`, `bar()` and `baz()`, which all have tests implemented in the tests/ folder, and you can run them using the `pytest` command as shown above.

Those who tried to create such a package manually know that quite often something does not work — an import does not work, `pytest` does not see the package, and the like. When using `makepackage`, you get a fully working structure of the package. The only thing you need to do is to replace the existing functions with your functions, and of course to adapt the package to this change.


> `makepackage` comes with some functionalities that you can get rid of:
>> * a conftest.py file in the tests/ folder
>> * simple annotations in the `foo()`, `bar()` and `baz()` functions of the newly created package
>> * `doctest`s in the above functions


# Notes on further development of your package

As mentioned before, the first step is to fill in several fields in setup.py and author in LICENSE. Then you need to create a virtual environment, in which you install the package in the editable mode. And that's all you need to start development. 

From now on, you're on your own. However, a package created using `makepackage` comes with some help for inexperienced users. They can see how to write tests (using `pytest`), how to use a conftest.py file (for `pytest`ing), how to write fixtures and use parametrized tests (again, for `pytest`ing), how to import the package's modules and functions, and the like. These are just some basic development tools. 

There is one thing I'd like to stress, and it's related to imports (actually, imports sometimes happen to pose some unexpected problems during Python coding). When you add a new module to the source folder (in our example, this is ziuziu/), e.g., ziuziu/another_ziuziu.py, then in the main `ziuziu` module you can import it as `from ziuziu import another_ziuziu` or `from ziuziu.another_ziuziu import another_foo`. Note that the regular approach you would use, that is, `import another_ziuziu`, will not work here.


## Testing

Testing of `makepackage` combines shell scripts and `pytest`. Therefore, running tests on Linux and Windows requires running different shell scripts. You will learn more from [here](tests/README.md).
