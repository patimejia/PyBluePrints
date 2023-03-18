import os

def create_directory(path):
    os.makedirs(path)


def create_file(path):
    with open(path, "w") as file:
        pass

def create_basic_structure(output_path):
    create_directory(os.path.join(output_path, "src"))
    create_directory(os.path.join(output_path, "tests"))

    create_file(os.path.join(output_path, "src", "main.py"))
    create_file(os.path.join(output_path, "tests", "test_main.py"))

def create_intermediate_structure(output_path):
    create_basic_structure(output_path)
    create_directory(os.path.join(output_path, "src", "utils"))

    create_file(os.path.join(output_path, "src", "utils", "helpers.py"))
    create_file(os.path.join(output_path, "tests", "test_helpers.py"))

def create_advanced_structure(output_path):
    create_intermediate_structure(output_path)
    create_directory(os.path.join(output_path, "src", "services"))

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
