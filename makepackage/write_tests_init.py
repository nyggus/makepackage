from pathlib import Path


def write_tests_init(path: Path) -> None:
    with open(path / "__init__.py", "w") as f:
        f.write("")
