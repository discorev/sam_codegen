#!/usr/bin/env python

import re
from setuptools import setup, find_packages
import pathlib


def file_path(file: str) -> pathlib.Path:
    """Return a path object for the given file name."""
    return pathlib.Path(__file__).parent / file


def read_version():
    """Read the version number of the cli."""
    content = file_path("sam_codegen/__init__.py").read_text()
    return re.search(r"__version__ = \"([^']+)\"", content).group(1)


def read_requirements(req: str):
    """Read requirements file into an array of requirements."""
    with file_path(req).open() as f:
        return [line.strip() for line in f if not line.strip().startswith("#")]


setup(
    name="sam-codegen",
    version=read_version(),
    description="AWS SAM code generator",
    long_description=file_path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Ollie",
    url="https://github.com/discorev/sam_codegen",
    packages=find_packages(exclude=["tests.*", "tests"]),
    # Support Python 3.7 or greater
    python_requires=">=3.7, <=4.0, !=4.0",
    entry_points={"console_scripts": ["sgc=sam_codegen.cli.main:cli"]},
    install_requires=read_requirements("requirements.txt"),
    include_package_data=True,
)
