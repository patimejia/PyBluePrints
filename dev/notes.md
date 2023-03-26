Package and distribute your project using the following command:

`python setup.py sdist`

This command will create a source distribution of your package in the dist folder.

To upload the package to the Python Package Index (PyPI), you can use `twine`. First, install `twine` if you haven't already:

```
pip install twine
```

Then, upload your package to PyPI using `twine`:

```
twine upload dist/*
```

## Resolving PyPI Upload Error: Incrementing Version and Rebuilding Package

Delete the dist and build directories to remove old builds:

```
rm -rf dist build
```

Increment the version number in your `setup.py` file, for example:

```
setup(
    ...
    version="0.1.1",

    ...
)
```

Re-create the source distribution and wheel file by running, build the package:

```
python setup.py sdist bdist_wheel
```

Upload the new package to PyPI using twine

```
twine upload dist/*
```

Make sure you have followed all these steps and removed the old files from the `dist` and `build` folders before uploading the new package to avoid confusion.
