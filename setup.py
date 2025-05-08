from setuptools import setup, find_packages

setup(
    name="python_package",
    version="0.1.0",
    author="Aadit",
    author_email="aaditsule0605@gmail.com",
    description="A sample Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aaditsule/python_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
