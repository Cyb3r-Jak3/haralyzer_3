#!/usr/bin/env python
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_reqs = ['cached-property',
                'python-dateutil',
                "six >= 1.13.0"]

if sys.version_info < (3, 4):
    install_reqs.extend([
        "backports.statistics",
    ])
test_requirements = ['pytest-cov',
                     'python-coveralls', ]

readme = open('README.rst').read()

setup(
        name="haralyzer_3",
        version="1.8.0",
        description="A Python 3 framework for getting useful stuff out of HAR files",
        long_description=readme,
        author="Justin Crown",
        author_email="justincrown1@gmail.com",
        url="https://github.com/Cyb3r-Jak3/haralyzer_3",
        download_url="https://github.com/mrname/haralyzer/tarball/1.0",
        packages=[
            "haralyzer_3"
        ],
        package_dir={"haralyzer_3": "haralyzer_3"},
        tests_require=test_requirements,
        install_requires=install_reqs,
        extras_require={
        },
        license="MIT",
        zip_safe=False,
        keywords="har",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
)
