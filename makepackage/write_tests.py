from pathlib import Path


def write_tests(path: Path, package_name: str) -> None:
    with open(path / f"test_{package_name}.py", "w") as f:
        f.write(
            f"""import pytest
from {package_name}.{package_name} import foo, bar, baz


@pytest.mark.parametrize(
    "test_input,expected",
    [(2, 4), (3, 9), (100, 10000), (1.2, 1.44), (-1, 1), (-2, 4), (-50, 2500),
])
def test_foo(test_input, expected):
    assert foo(test_input) == expected


def test_bar_basic():
    assert bar("AAAaA") == "aaaaa"


def test_bar(strings):
    for string in strings:
        assert not any(s.isupper() for s in bar(string))


def test_baz_basic():
    assert baz("AAAaA") == "AAAAA"


def test_baz(strings):
    for string in strings:
        assert not any(s.islower() for s in baz(string))

"""
        )
