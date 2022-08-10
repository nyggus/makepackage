from pathlib import Path


def write_CLI_main(path: Path, package_name: str) -> None:
    CLI_main = f"""from {package_name} import foo, bar, baz


def main():
    print("Running all {package_name} functions via"
        " the command-line command ($ {package_name}): "
    )
    print(
        "This is foo(): ", foo(1),
        "Function bar() uses str.lower() method:", bar("Lower"),
        "Function baz() uses str.upper() method:", baz("Upper")
    )


if __name__ == "__main__":
    main()
"""
    with open(path / "__main__.py", "w") as f:
        f.write(CLI_main)
