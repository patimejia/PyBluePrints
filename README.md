# Project Scaffolds

A Python-based generator for creating well-organized project structures using best practices, `unittest`, `pytest`, and the Python Standard Library. Supports basic, intermediate, and advanced folder configurations for maintainable projects.

## Why is File Structure Important?

A well-organized file structure is crucial for any software project. It makes your code easier to understand, navigate, and maintain. Following best practices for file structure ensures consistency across projects, which can be especially helpful when **collaborating** with others or when you revisit your project after some time.

## Best Practices

Some best practices for organizing Python projects include:

- Separating source code and test code into different folders.
- Using meaningful and descriptive names for files and folders.
- Including a `README.md` file to provide an overview and usage instructions.
- Adding a `LICENSE` file to specify the terms under which the project can be used.
- Grouping related files together, such as scripts for different project structures.

## Project Structures

This project scaffold generator supports three different file structures:

### Basic

```shell
basic_project/
│
├── LICENSE
├── README.md
│
├── src/
│ ├── init.py
│ └── main.py
│
└── tests/
├── init.py
└── test_main.py
```

### Intermediate

```shell
intermediate_project/
│
├── LICENSE
├── README.md
│
├── src/
│ ├── init.py
│ ├── main.py
│ └── utils/
│ ├── init.py
│ └── helpers.py
│
└── tests/
├── init.py
├── test_main.py
└── test_helpers.py
```

### Advanced

```shell
advanced_project/
│
├── LICENSE
├── README.md
│
├── src/
│ ├── init.py
│ ├── main.py
│ ├── utils/
│ │ ├── init.py
│ │ └── helpers.py
│ └── services/
│ ├── init.py
│ └── service.py
│
└── tests/
├── init.py
├── test_main.py
├── test_helpers.py
└── test_service.py
```

For more information on installation, usage, and testing, refer to the respective sections in this `README.md` file.

## Contributing

Contributions to this repository are welcome and encouraged! If you have suggestions for improving the file structure or the code organization, please submit a pull request. Let's keep improving our best practices and methods for organizing code and file directories in Python projects!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
