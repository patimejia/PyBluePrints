from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="PyBlueprintMaker",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python-based project scaffolding tool for creating well-organized project structures using best practices, fixture, pytest, and the Python Standard Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/PyBlueprintMaker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords="project-scaffolding project-structure fixture pytest",
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "PyBlueprintMaker=PyBlueprintMaker.main:main",
        ],
    },
)
