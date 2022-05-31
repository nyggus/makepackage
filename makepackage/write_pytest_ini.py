import pathlib


def write_pytest_ini(path: pathlib.Path) -> None:
    with open(path / "pytest.ini", "w") as f:
        f.write(
            """[pytest]
testpaths = tests
"""
        )
