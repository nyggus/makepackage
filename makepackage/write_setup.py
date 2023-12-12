from pathlib import Path


def write_setup(path: Path, package_name: str, CLI: bool) -> None:
    setup = """from setuptools import setup\n\nsetup()\n"""

    with open(path / "setup.py", "w") as f:
        f.write(setup)
