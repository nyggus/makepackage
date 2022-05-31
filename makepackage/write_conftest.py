import pathlib


def write_conftest(path: pathlib.Path) -> None:
    with open(path / "conftest.py", "w") as f:
        f.write(
            """import pytest

@pytest.fixture
def strings():
    return (
        "Whatever string",
        "Shout Bamalama!",
        "Sing a song about statistical models.", 
    )

"""
        )
