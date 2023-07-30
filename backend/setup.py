"""A setuptools based setup module.
Authoritative references:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path, getenv

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="kubernetes-env-manager",
    version=getenv("APP_VERSION", "0.0.0"),
    description="Manager for kubernetes environment",
    long_description=long_description,
    packages=find_packages(exclude=["doc"]),
    # source code layout
    namespace_packages=["package"],
    # Generating the command-line tool
    entry_points={"console_scripts": ["kubernetes-env-manager=package.run:prod"]},
    # author and license
    author="Ivan Djuraki",
    author_email="ivandjuraki@protonmail.com",
)
