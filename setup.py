# -*- coding: utf-8 -*-
from setuptools import setup, find_packages  # noqa: H301

with open("README.md") as f:
    long_description = f.read()

NAME = "refurbished"
REQUIRES = [
    "beautifulsoup4 >= 4.11.1",
    "click == 8.1.3",
    "price-parser == 0.3.4",
    "pydantic == 1.10.2",
    "requests >= 2.28.1",
    "rich >= 12.6.0",
]

setup(
    name=NAME,
    version="0.11.0",
    description="Library to search refurbished products on the Apple Store",
    author="Maurizio Branca",
    author_email="maurizio.branca@gmail.com",
    url="https://github.com/zmoog/refurbished",
    scripts=['cli/rfrb'],
    keywords=[],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
