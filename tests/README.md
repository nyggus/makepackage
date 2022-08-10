# Testing of `makepackage`

The tests of `makepackage` consist of several steps:
* package `pkgNoCLI` (`pkgNoCLIWin` in Windows) is created (without CLI funtionality), using a shell script
* the tests in package `pkgNoCLI`/`pkgNoCLIWin` are run (both `pytest`s and `doctest`s)
fine
* package `pkgCLIWithCLI` (`pkgCLIWithCLIWin`) is created (with CLI funtionality), using a shell script
* the tests in package `pkgCLIWithCLI` (`pkgCLIWithCLIWin`) are run (both `pytest`s and `doctest`s)
* `makepackage` tests (using `pytest`) whether the resulting folder and file structure in the both these packages is fine
* all testing files are cleaned up

All those steps are collected in shell scripts:
* [run_tests.sh](run_tests.sh) for Linux
* [run_tests.bat](run_tests.bat) for Windows

Thus, enough to run one of these two scripts and all the steps will be done one by one. Observe what is happening during the process, as for instance `pytest` is run three times:
* for `pkgNoCLI`/`pkgNoCLIWin`
* for `pkgCLIWithCLI`/`pkgWithCLIWin`
* for `makepackage`, based on `pkgNoCLI`/`pkgNoCLIWin` and `pkgWithCLI`/`pkgWithCLIWin`
