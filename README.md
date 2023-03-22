# Project Scaffolds

A Python-based project scaffolding tool for creating well-organized project structures using best practices, `fixture`, `pytest`, and the Python Standard Library. Supports basic, intermediate, and advanced folder configurations for maintainable projects.

## Why is File Structure Important?

A well-organized file structure is crucial for any software project. It makes your code easier to understand, navigate, and maintain. Following best practices for file structure ensures consistency across projects, which can be especially helpful when **collaborating** with others or when you revisit your project after some time.

## Best Practices

Some best practices for organizing Python projects include:

- Separating source code and test code into different folders.
- Using meaningful and descriptive names for files and folders.
- Including a `README.md` file to provide an overview and usage instructions.
- Adding a `LICENSE` file to specify the terms under which the project can be used.
- Grouping related files together, such as scripts for different project structures.

## Running the Project Scaffold Generator

To run the project scaffold generator, follow these steps:

1. Clone this repository to your local machine.
2. Open the terminal and navigate to the project directory.
3. Run the `main.py` script to generate the project structure of your choice.

For example, to generate an `extended` project structure, run the following command:

```bash
python src/main.py ../my_new_project/ extended
```

This will create a new directory called `my_new_project` in the parent directory of the project scaffold generator. The `extended` argument specifies the project structure to generate. The available options are `basic`, `intermediate`, `advanced`, and `extended`.

To run the main.py script, you can use the command line. First, open a terminal or command prompt, navigate to the directory containing the main.py file, and then run the following command:

```
python main.py <output_path> <structure>
```

Replace `<output_path>` with the desired output path for the project structure you want to create and `<structure>` with the structure you want to create, which can be one of the following options: `basic`, `intermediate`, `advanced`, `extended`, or `modular`.

For example, to create a basic project structure in a folder called "my_project", you would run:

```
python main.py my_project basic
```

Similarly, to create a modular project structure in a folder called "my_modular_project", you would run:

python src/main.py ../my_new_project/ extended

`python main.py ../my_modular_project/ modular`

Make sure you have Python installed on your system, and that the terminal or command prompt is pointing to the correct version of Python. If you have multiple versions installed, you may need to use `python3` instead of `python`.

## Project Structures

This project scaffold generator supports three different file structures:

### Basic

```
basic_project/
├── .gitignore
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   └── main.py
└── tests
    ├── __init__.py
    └── test_main.py
```

### Intermediate

```
intermediate_project/
├── .gitignore
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── main.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
└── tests
    ├── __init__.py
    ├── test_helpers.py
    └── test_main.py
```

### Advanced

```
advanced_project/
├── .gitignore
├── README.md
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
└── tests
    ├── __init__.py
    ├── test_helpers.py
    ├── test_main.py
    └── test_service.py
```

### Extended

```
extended_project/
├── .gitignore
├── README.md
├── requirements.txt
├── assets
│   └── images
├── data
│   ├── input
│   ├── intermediate
│   └── output
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── services
│   │   ├── __init__.py
│   │   └── service.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
└── tests
    ├── __init__.py
    ├── test_helpers.py
    ├── test_main.py
    └── test_service.py
```

# Modular

```
project_name/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── service.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_service.py
│   └── test_helpers.py
│
├── assets/
│   └── images/
│
├── data/
│   ├── input/
│   ├── intermediate/
│   └── output/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Customization

This project scaffold generator is designed to be flexible, allowing you to customize the generated file structure according to your needs. If you want to further tailor the project structure, you can make modifications to the `main.py` script.

Here are some steps you can follow to customize the project structure:

1. Open the `main.py` script in your preferred text editor or IDE.
2. Locate the functions for each project structure: `create_basic_structure`, `create_intermediate_structure`, `create_advanced_structure`, and `create_extended_structure`.
3. Modify these functions to add, remove, or rename directories and files as desired.
   - To create a new directory, use the `create_directory()` function with the desired path.
   - To create a new file, use the `create_file()` function with the desired path.
4. Save your changes and run the modified script to generate the updated project structure.

## Contributing

Contributions to this repository are welcome and encouraged! If you have suggestions for improving the file structure or the code organization, please submit a pull request. Let's keep improving our best practices and methods for organizing code and file directories in Python projects!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
