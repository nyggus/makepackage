# Testing of `makepackage`

The tests of `makepackage` consist of several steps:
* package `pkg` is created (without CLI funtionality), using a shell script
* the tests in package `pkg` are run (both `pytest`s and `doctest`s)
* `makepackage` tests (using `pytest`) whether the resulting folder and file structure in the `pkg` package is fine
* package `pkgCLI` is created (with CLI funtionality), using a shell script
* the tests in package `pkgCLI` are run (both `pytest`s and `doctest`s)
* `makepackage` tests (using `pytest`) whether the resulting folder and file structure in the `pkgCLI` package is fine
* all testing files are cleaned up

All those steps are collected in shell scripts:
* run_tests.sh for Linux
* run_tests.bat for Windows

Thus, enough to run one of these two scripts and all the steps will be done one by one. Observe what is happening during the process, as for instance `pytest` is run three times:
* for `pkg`
* for `pkgCLI`
* for `makepackage`, based on `pkg` and `pkgCLI`
