# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="pyflight",
    version="0.0.1",
    description="A Python Wrapper around Google's QPX Express API",
    license="MIT",
    author="Volcyy",
    packages=find_packages(),
    install_requires=['aiohttp', ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
