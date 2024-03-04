# `makepackage`: A Python package for packaging Python code

## Installation

Install the package from [PyPi](https://pypi.org/project/makepackage/):

```shell
$ pip install makepackage
```


## TL;DR: How to use `makepackage`

To create a package that does not need a command-line argument, go to a directory where you want to create the structure of your package and run in shell

```shell
$ makepackage mypackage
```

where `mypackage` is the name of your package. That's it! You will have a self-standing package that you can now develop. Remember to fill in `[MAKEPACKAGE]` fields in pyproject.toml and LICENSE.

If you want to create a package with a command-line argument, add a `cli` flag after the name of the package:

```shell
$ makepackage mypackage cli
```

and here you are. Your package will get the command-line argument that is the same as the package's name.

Now let's go into detail.


## Rationale and background

Organizing Python code in a package has a lot of advantages and can significantly simplify development — but the first hours can be tricky. To facilitate this process, you can use tools such as [Cookiecutter](https://cookiecutter.readthedocs.io/), but they themselves are quite advanced and offer a lot of functionalities that you need to learn — quite often, this complexity makes development more difficult, sometimes changing the hours spent with the tool into a nightmare. 

To facilitate this step, I created a package template and have been using it for about a year. Life got easier. But the template required some manual work that could be automated. This is when I thought that a script would be better, so I wrote one. It worked fine indeed, and things got even easier. And then I thought, as this is so useful for me, why not make it useful for others? So, I made this package, and now you can use it just like me.

`makepackage` offers only one function, available via shell. The only thing you need to do is to install `makepackage` (preferably in a virtual environment you will use only to create new packages) and run a simple shell command (which works under both Linux and Windows). The command, as you will see below, takes one required argument: a package's name; you can add `--cli` to create a CLI package, as otherwise (without the flag) it will not have command-line interface.

The use of `makepackage` is very simple, but this does not come without costs: it creates just one type of structure, though you can change it manually:
* you have to fill in some fields in pyproject.toml
* pyproject.toml will include `pytest`, `wheel`, `black`, `mypy` and `setuptools` in the `dev` mode; you can remove them manually before installing the package in the editable mode
* the package will use `pytest` for unit testing and `doctest` for documentation testing

> You will find annotated code in `ziuziu` (given the simplicity of the functions, the annotations are very simple), and you can run `mypy` on it, with success.

The idea behind `makepackage` is to offer a tool that creates a working package with a simple but common structure, which can be then extended and developed. And indeed, you will find in it tests (both `pytest`s and `doctest`s) that pass; you can install the package in the editable mode, and after that you will be able to import it. So, the resulting package is just fine, and you can immediately move to development.

> `makepackage` offers one of many possible structures, and it assumes you will use `pytest` for testing. If you want to use other solutions, you should either create a package manually or use another tool.


## Using `makepackage`

> The [tests](tests/) folder contains six shell scripts. Two of them show how to use `makepackage` in Linux, and two others do the same for Windows. One of the scripts shows how to create a package that does not need command-line interface while the other with CLI. Check out these two files for Linux: [`makepackage` without CLI](tests/run_makepackage_no_CLI.sh) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.sh); and for Windows, these two files: [`makepackage` without CLI](tests/run_makepackage_no_CLI.bat) and [`makepackage` with CLI](tests/run_makepackage_with_CLI.bat).

It's best to install and use `makepackage` in a virtual environment. So, for example,

```shell
$ python -m venv venv-makepackage
$ venv-package/bin/activate
(venv-makepackage) $ python -m pip install makepackage
```

> Examples show Linux commands, but any Windows user will know how to replace them with the corresponding Windows commands (though most commands will be the same in Linux and Windows; you simply need to change paths when activating a virtual environment in Windows).

Now that we have activated the virtual environment and installed `makepackage` in it, we are ready to create a package of our own. First, navigate to a folder where you want to create the package, and run the following command:

```shell
(venv-makepackage) $ makepackage ziuziu
```

This creates a `ziuziu` package; `ziuziu` will not have command-line interface. You will now see a ziuziu folder:

```shell
(venv-makepackage) $ ls
ziuziu
```

If you want to create a package with command-line interface, use a command-line flag `--cli`, like this:

```shell
(venv-makepackage) $ makepackage ziuziu --cli
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


> When you create a package using `makepackage`, you can read the README file of the new package. It contains some essential information about package development, such as building the package, installing it, and uploading to PyPi.

## Structure of a package created using `makepackage`

You can use various structures to create a Python package. `makepackage` uses one of them, a simple (though not the simplest) but quite common one. You will see the following structure of the ziuziu/ folder (so, of the `ziuziu` package):

```shell
.
+-- .gitignore
+-- LICENSE
+-- README.md
+-- pytest.ini
+-- pyproject.toml
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
* the package is developed using `pytest` and `doctest` (you will find both implemented in the code of `ziuziu`)
* MIT license is used (you can change it to any license you want, but remember also to change the license in pyproject.toml)
* in the development mode, `pytest`, `wheel`, `black` and `mypy` packages are additionally installed in the virtual environment (used for development); they are *not* installed when one installs the package from PyPi
* you will need to fill in pyproject.toml in several places (namely, fields `authors`, `description`, `classifiers` and `project_urls`) and LICENSE in one place; you can easily find those places, as they are indicated with the `"[MAKEPACKAGE]"` mark.

Of course, this is a starting point, and you can now extend the package however you want. Once installed, `ziuziu` (or however you name the package) works. It has three functions, `foo()`, `bar()` and `baz()`, which all have tests implemented in the tests/ folder, and you can run them using the `pytest` command as shown above.

Those who tried to create such a package manually know that quite often something does not work — an import does not work, `pytest` does not see the package, and the like. When using `makepackage`, you get a fully working structure of the package. The only thing you need to do is to replace the existing functions with your functions, and of course to adapt the package to this change.


> `makepackage` comes with some functionalities that you can get rid of:
>> * a conftest.py file in the tests/ folder
>> * simple annotations in the `foo()`, `bar()` and `baz()` functions of the newly created package
>> * `doctest`s in the above functions
>> * packages installed in the editable mode


# Notes on further development of your package

As mentioned before, the first step is to fill in several fields in pyproject.toml and author in LICENSE. Then you need to create a virtual environment, in which you install the package in the editable mode. And that's all you need to start development. 

From now on, you're on your own. However, a package created using `makepackage` comes with some help for inexperienced users. They can see how to write tests (using `pytest`), how to use a conftest.py file (for `pytest`ing), how to write fixtures and parametrized tests (again for `pytest`ing), how to import the package's modules and functions, how to write `doctest`s, and the like. These are just some basic development tools. 

There is one thing I'd like to stress, and it's related to imports. (The truth is, imports sometimes happen to pose some unexpected problems during Python coding). When you add a new module to the source folder (in our example, this is ziuziu/), e.g., ziuziu/another_ziuziu.py, then in the main `ziuziu` module you can import it as `from ziuziu import another_ziuziu` or `from ziuziu.another_ziuziu import another_foo`. Note that the regular approach you would use, that is, `import another_ziuziu`, will not work here.


## Testing

Testing of `makepackage` combines shell scripts and `pytest`. Therefore, running tests on Linux and Windows requires running different shell scripts. You will learn more from [here](tests/README.md).


## Contribution

Everyone is invited to develop `makepackage`. You can submit an issue or a pull request. Nonetheless, be aware that I will only accept proposals that
* keep the current API of the package, unless the proposed change is so great that the cost of changing the API is relatively small compared to what the new functionality offers
* are covered by unit tests
* are well documented (if needed)
* are coded in a similar style that the current code uses
* work under both Windows and Linux

Below, you can read more about these aspects.

> Do remember to increment `makepackage`'s version. Use [semantic versioning 2.0.0](https://semver.org/).

In technical terms, to contribute,
* fork the repository and clone it to your machine
* create a new branch: `$ git checkout -b new-branch`, where `new-branch` is the name of a branch, so remember to name it in a way that reflects what the branch changes (and please, do not use the name of `new-branch` or similar)
* once you're done with all the changes and are ready to commit the changes, you can use `git add path` to add each file separately (`path` being a relative path to a file you want to commit); after each such command, do `$ git commit -m "What I did"`, the comment explaining what is changed in the committed file. If you want to add all the files at the same time, do `$ git add .`.
* `$ git push --set-upstream origin new-branch` — this will create the branch in the repo and will push the changes to it.
* create a pull request to the original repository; when doing so, please explain the changes in detail

If someone else is developing `makepackage` at the same time, you may have to solve the resulting conflicts. How to say it... be patient and don't break down! Don't break down your computer, either! Keep your nerves in check!

Now, you can sit and wait for a review of your proposal; use this time for thinking about how to improve the package even more :smiley:. 


#### Keep the current API of the package

This, for instance, means that `makepackage`'s API does not offer different licences, structures of the root folder, and the like. Also, the API does not offer numerous arguments to enable the user to fill in the required fields of pyproject.toml; the user can do it directly in the file, an approach that is easier than providing this information through command-line arguments. No GUI, too: just a simple shell command.

The simpler the API, the easier the package is to use. The idea behind `makepackage` was to bring a *really* simple API to create a package. This simplicity cannot come without cost, but the cost does not seem that great. True, if one wants to create a different organization of the package or wants to use `unittest` instead of `pytest`, then one will have to choose a different tool or do it manually. This is the main cost of simplicity we have to pay, but had `makepackage` enabled the user to choose from different options, the package's API would have been far more complicated. This would mean the main purpose behind creating the package — crreating the structure of a Python package in an easy way — would not have been accomplished. 

Simply put, `makepackage` has a simple API and does not offer too many choices, and I want to keep it that way.


#### Cover all functionality by unit tests

Add unit tests to every new functionality or change, unless the change does not change the package's functioning whatsoever. Remember that `makepackage` is tested with `pytest` and `doctest`.


#### Use readable and sufficient documentation

If you add a new functionality or change the existing one, you have to document it in documentation: README and docstrings. Of course, don't overdo, but note that this README is long and detailed. It has the [TL;DR: How to use makepackage](#tldr-how-to-use-makepackage) section, which is short and concise. Then, we go deep when explaining the details. Keep this approach.


#### Maintain the current coding style

This is important. Keep the current style, and please use `black` to format code. By coding style I do not only mean what `black` changes; I mean other important things, such as the following:

* Have you noticed that the only classes that are defined in the package are those for custom exceptions? Try not to change that and do not base any new functionality on a class, unless this is a better and more natural approach.
* `makepackage` uses custom exceptions to handle the user's mistakes. Throwing custom errors inside `makepackage` functions improves traceback, by using well-named exception classes and moving the traceback into the actual location in code where the exception occurred.


#### Work under both Windows and Linux

`makepackage` works in both these OSs, so if you want to propose something new, make sure this works under both these OSs. If you have problems with doing so, please contant the repo's maintainer.

However, if you can check if `makepackage` works fine under a different OS, please do so and add it to this section.
