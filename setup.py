# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:36:56 2021

@author: myersau3
"""

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="dynamical_networks", # Replace with your own username
    version="0.1.4",
    author="Audun Myers",
    author_email="myersau3@msu.edu",
    description="A package for dynamical networks simulations and analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myersau3/Dynamical_Networks",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
