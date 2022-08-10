from pathlib import Path

module = '''def foo(x: int) -> int:
    """Calculate square of x.
    
    >>> foo(2)
    4
    >>> foo(100)
    10000
    """
    return x**2


def bar(string: str) -> str:
    """Use method .lower() to a string.

    Args:
        string (str): a string to be manipulated

    Returns:
        str: a manipulated string
    
    >>> bar("Whatever!")
    'whatever!'
    >>> bar("AAaa...!")
    'aaaa...!'
    """
    return string.lower()


def baz(string: str) -> str:
    """Use method .upper() to a string.

    Args:
        string (str): a string to be manipulated

    Returns:
        str: a manipulated string
    
    >>> baz("Whatever!")
    'WHATEVER!'
    >>> baz("AAaa...!")
    'AAAA...!'
    """
    return string.upper()
'''


def write_module(path: Path, package_name: str) -> None:
    with open(path / f"{package_name}.py", "w") as f:
        f.write(module)
