#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'accepton'))
from version import VERSION


def parse_requirements(path):
    """Rudimentary parser for the `requirements.txt` file

    We just want to separate regular packages from links to pass them to the
    `install_requires` and `dependency_links` params of the `setup()` function
    properly.

    Borrowed from the httpretty library by Gabriel Falcao, which is licensed
    under the MIT license.

    https://github.com/gabrielfalcao/HTTPretty/blob/10cbee3471/setup.py#L50
    """
    try:
        requirements = map(str.strip, local_file(path).splitlines())
    except IOError:
        raise RuntimeError("Couldn't find the %s file" % path)

    links, packages = [], []

    for requirement in requirements:
        if not requirement:
            continue
        if 'http:' in requirement or 'https:' in requirement:
            links.append(requirement)
            name, version = re.findall("\#egg=([^\-]+)-(.+$)", requirement)[0]
            packages.append("{0}=={1}".format(name, version))
        else:
            packages.append(requirement)

    return packages, links

local_file = lambda *f: \
    open(os.path.join(os.path.dirname(__file__), *f)).read()

install_requires, dependency_links = parse_requirements('requirements.txt')

setup(
    name="accepton",
    version=VERSION,
    description="AcceptOn Python library",
    long_description=local_file("README.rst"),
    classifiers=[
        "Development Status :: 4 - Beta",
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
    url="http://developers.accepton.com",
    license="MIT",
    packages=find_packages(exclude=["*tests*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    test_suite="tests",
    tests_require=parse_requirements("requirements-test.txt")
)
