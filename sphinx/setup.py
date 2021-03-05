import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="dynamical networks", # Replace with your own username
    version="0.0.1",
    author="Audun Myers",
    author_email="myersau3@msu.edu",
    description="A dynamical networks package for modeling and analysis",
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
