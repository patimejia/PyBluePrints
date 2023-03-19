import os
import argparse

def create_directory(path):
    os.makedirs(path)

def create_file(path):
    with open(path, "w") as file:
        pass

def create_basic_structure(output_path):
    create_directory(os.path.join(output_path, "src"))
    create_directory(os.path.join(output_path, "tests"))

    create_file(os.path.join(output_path, ".gitignore"))
    create_file(os.path.join(output_path, "README.md"))
    create_file(os.path.join(output_path, "requirements.txt"))
    create_file(os.path.join(output_path, "src", "__init__.py"))
    create_file(os.path.join(output_path, "tests", "__init__.py"))
    create_file(os.path.join(output_path, "src", "main.py"))
    create_file(os.path.join(output_path, "tests", "test_main.py"))

def create_intermediate_structure(output_path):
    create_basic_structure(output_path)
    create_directory(os.path.join(output_path, "src", "utils"))

    create_file(os.path.join(output_path, "src", "utils", "__init__.py"))
    create_file(os.path.join(output_path, "src", "utils", "helpers.py"))
    create_file(os.path.join(output_path, "tests", "test_helpers.py"))

def create_advanced_structure(output_path):
    create_intermediate_structure(output_path)
    create_directory(os.path.join(output_path, "src", "services"))

    create_file(os.path.join(output_path, "src", "services", "__init__.py"))
    create_file(os.path.join(output_path, "src", "services", "service.py"))
    create_file(os.path.join(output_path, "tests", "test_service.py"))

def create_extended_structure(output_path):
    create_advanced_structure(output_path)
    create_directory(os.path.join(output_path, "assets"))
    create_directory(os.path.join(output_path, "data"))
    create_directory(os.path.join(output_path, "assets", "images"))
    create_directory(os.path.join(output_path, "data", "input"))
    create_directory(os.path.join(output_path, "data", "intermediate"))
    create_directory(os.path.join(output_path, "data", "output"))

def main(output_path, structure):
    if structure == "basic":
        create_basic_structure(output_path)
    elif structure == "intermediate":
        create_intermediate_structure(output_path)
    elif structure == "advanced":
        create_advanced_structure(output_path)
    elif structure == "extended":
        create_extended_structure(output_path)
    else:
        print(f"Invalid structure '{structure}'. Choose from 'basic', 'intermediate', 'advanced', or 'extended'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a project structure.")
    parser.add_argument("output_path", help="The desired output path for the project structure.")
    parser.add_argument("structure", help="The project structure to create: basic, intermediate, advanced, or extended.")

    args = parser.parse_args()

    main(args.output_path, args.structure)
