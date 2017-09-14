# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="pyflight",
    version='0.1.3',
    description="An asynchronous Wrapper around Google's QPX Express API",
    license="MIT",
    author="Volcyy",
    packages=find_packages(exclude=[
        "build", "dist", "docs", "examples",
        "pyflight.egg-info", "tests", "venv"
    ]),
    url="https://github.com/Volcyy/pyflight",
    install_requires=['aiohttp', 'requests'],
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ])
