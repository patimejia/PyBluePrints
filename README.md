# PyBlueprintMaker

`PyBlueprintMaker` is a Python-based project scaffolding tool that helps you create well-organized project structures using best-practices, `fixtures`, `pytest`, and the Python Standard Library. With support for `basic` to `modular` folder configurations and comprehensive testing, PyBlueprintMaker is the ultimate solution for maintainable projects.

## Why is File Structure Important?

A well-organized file structure is crucial for any software project. It makes your code easier to understand, navigate, and maintain. Following best practices for file structure ensures consistency across projects, which can be especially helpful when collaborating with others or when you revisit your project after some time.

## Best Practices

Some best practices for organizing Python projects include:

- Separating source code and test code into different folders.
- Using meaningful and descriptive names for files and folders.
- Including a `README.md` file to provide an overview and usage instructions.
- Adding a `LICENSE` file to specify the terms under which the project can be used.
- Grouping related files together, such as scripts for different project structures.

## Installation

To install PyBlueprintMaker, you can use pip:

```
pip install PyBlueprintMaker
```

Alternatively, you can install from source by cloning this repository and running:

```
python setup.py install
```

Make sure to also include any necessary dependencies that are not automatically installed.

## Usage

To use PyBlueprintMaker, run the following command:

```
PyBlueprintMaker [output_path] [structure]
```

Where `output_path` is the desired output path for the project structure and structure is the project structure to create. The supported structures are` basic`, `intermediate`, `advanced`, `extended`, or `modular`.

For example, to create a `basic` project structure in a folder named `my_project`, run the following command:

```
PyBlueprintMaker my_project basic
```

## Outputs and Structures

PyBlueprintMaker supports the following project structures:

- `basic`: This structure is intended for simple projects with a single Python script and a `README.md` file.

These folder structures are designed to accommodate various aspects of data architecture and data science projects, including data storage, version control, automated testing, containerization, and reproducibility. The most advanced structure is intended for projects with complex configurations and additional tools for automation and collaboration.

## Contributing

If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License

PyBlueprintMaker is licensed under the MIT License.

## Support

If you like this project, please consider sharing a coffee. Thank you! 🦉

<a href="https://www.buymeacoffee.com/patimejiaS" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
