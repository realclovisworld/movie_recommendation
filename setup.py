from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Clovis Atiki"
SRC_REPO = 'src'
LIST_OF_PACKAGES = ['streamlit']

setup(
    name="SRC_REPO",
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email="atikiclovis0@gmail.com",
    description="A simple package for movie recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package = [SRC_REPO],
    pythom_requires='>=3.7',
    install_requires=LIST_OF_PACKAGES,
)