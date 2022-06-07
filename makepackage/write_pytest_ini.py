from pathlib import Path


def write_pytest_ini(path: Path) -> None:
    with open(path / "pytest.ini", "w") as f:
        f.write(
            """[pytest]
testpaths = tests
"""
        )
