import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="serverspeak",
    py_modules=["serverspeak, os, sys, torch, json"],
    version="1.0",
    description="",
    author="MrC",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True
)
