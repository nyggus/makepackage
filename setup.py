import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_requirements = {
    "dev": ["wheel", "black", "pytest", "mypy", ],
}

setuptools.setup(
    name="makepackage",
    version="0.1.1",
    author="Nyggus",
    author_email="nyggus@gmail.com",
    description="Creating a structure of a simple Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/nyggus/makepackage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "easycheck",
    ],
    python_requires=">=3.6",
    extras_require=extras_requirements,
    entry_points={
        "console_scripts": ["makepackage = makepackage.__main__:main"]
    },
)
