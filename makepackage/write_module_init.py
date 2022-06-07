from pathlib import Path


def write_module_init(path: Path, package_name: str) -> None:
    module_init = f"""from .{package_name} import foo, bar, baz
"""
    with open(path / "__init__.py", "w") as f:
        f.write(module_init)
