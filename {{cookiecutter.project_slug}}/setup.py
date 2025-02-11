#!/usr/bin/env python3

import setuptools

PACKAGE_NAME = "{{cookiecutter.project_slug}}"
DESCRIPTION = "{{cookiecutter.project_short_description}}"


setuptools.setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    package_data={PACKAGE_NAME: ["py.typed", "config/*.json", "templates/*.pdf"]},
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    description=DESCRIPTION,
    entry_points={
        "console_scripts": [
             "cli = {{cookiecutter.project_slug}}.cli:entry_point",
        ]
    },
)
