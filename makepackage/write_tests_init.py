def write_tests_init(path) -> None:
    with open(path / "__init__.py", "w") as f:
        f.write("")
