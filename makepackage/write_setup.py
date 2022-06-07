from pathlib import Path


def write_setup(path: Path, package_name: str, CLI: bool) -> None:
    setup = f"""import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_requirements = LEFT_CURLY_BRACKET
    "dev": ["wheel", "black", "pytest", "mypy"],
RIGHT_CURLY_BRACKET

setuptools.setup(
    name="{package_name}",
    version="0.1.0",
    author="[MAKEPACKAGE]",
    author_email="[MAKEPACKAGE]",
    description="[MAKEPACKAGE]",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="[MAKEPACKAGE]",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[],
    extras_require=extras_requirements,
    python_requires='>=3.8',
"""
    if CLI:
        setup += f"""    entry_points=LEFT_CURLY_BRACKET"console_scripts": ["{package_name} = {package_name}.__main__:main"]RIGHT_CURLY_BRACKET
)
"""
    else:
        setup += f")"

    setup = replace_curly_brackets(setup)
    with open(path / "setup.py", "w") as f:
        f.write(setup)


def replace_curly_brackets(string: str):
    """
    >>> replace_curly_brackets("LEFT_CURLY_BRACKETRIGHT_CURLY_BRACKET")
    '{}'
    >>> replace_curly_brackets(f"LEFT_CURLY_BRACKET{10*2}RIGHT_CURLY_BRACKET")
    '{20}'
    """
    return string.replace("LEFT_CURLY_BRACKET", "{").replace(
        "RIGHT_CURLY_BRACKET", "}"
    )
