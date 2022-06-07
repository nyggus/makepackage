from pathlib import Path


def write_conftest(path: Path) -> None:
    with open(path / "conftest.py", "w") as f:
        f.write(
            """import pytest

from typing import Tuple

@pytest.fixture
def strings() -> Tuple[str, str, str]:
    return (
        "Whatever string",
        "Shout Bamalama!",
        "Sing a song about statistical models.", 
    )

"""
        )
