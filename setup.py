# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert("README.md", 'rst')
except ImportError:
    long_description = open("README.md").read()

setup(
    name="pyflight",
    version='0.1.2',
    description="An asynchronous Wrapper around Google's QPX Express API",
    license="MIT",
    author="Volcyy",
    packages=find_packages(),
    url="https://github.com/Volcyy/pyflight",
    install_requires=['aiohttp', 'requests'],
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
