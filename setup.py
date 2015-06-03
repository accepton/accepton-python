#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'accepton'))
from version import VERSION

setup(
    name="accepton",
    version=VERSION,
    description="AcceptOn Python library",
    long_description=readme,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords=[],
    author="AcceptOn",
    author_email="developers@accepton.com",
    url="https://accepton.com",
    license="TODO",
    packages=["accepton"],
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
)
