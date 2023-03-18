import os
import shutil
import tempfile
from src import project_generator
import pytest


@pytest.fixture
def output_path():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


def test_create_basic_structure(output_path):
    project_generator.create_basic_structure(output_path)

    # Verify created folders and files
    assert os.path.exists(os.path.join(output_path, "src"))
    assert os.path.exists(os.path.join(output_path, "tests"))
    assert os.path.exists(os.path.join(output_path, "src", "main.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_main.py"))


def test_create_intermediate_structure(output_path):
    project_generator.create_intermediate_structure(output_path)

    # Verify created folders and files
    assert os.path.exists(os.path.join(output_path, "src"))
    assert os.path.exists(os.path.join(output_path, "tests"))
    assert os.path.exists(os.path.join(output_path, "src", "main.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_main.py"))
    assert os.path.exists(os.path.join(output_path, "src", "utils"))
    assert os.path.exists(os.path.join(output_path, "src", "utils", "helpers.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_helpers.py"))


def test_create_advanced_structure(output_path):
    project_generator.create_advanced_structure(output_path)

    # Verify created folders and files
    assert os.path.exists(os.path.join(output_path, "src"))
    assert os.path.exists(os.path.join(output_path, "tests"))
    assert os.path.exists(os.path.join(output_path, "src", "main.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_main.py"))
    assert os.path.exists(os.path.join(output_path, "src", "utils"))
    assert os.path.exists(os.path.join(output_path, "src", "utils", "helpers.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_helpers.py"))
    assert os.path.exists(os.path.join(output_path, "src", "services"))
    assert os.path.exists(os.path.join(output_path, "src", "services", "service.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_service.py"))

def test_create_extended_structure(output_path):
    project_generator.create_extended_structure(output_path)

    # Verify created folders and files
    assert os.path.exists(os.path.join(output_path, "src"))
    assert os.path.exists(os.path.join(output_path, "tests"))
    assert os.path.exists(os.path.join(output_path, "assets"))
    assert os.path.exists(os.path.join(output_path, "data"))
    assert os.path.exists(os.path.join(output_path, "src", "main.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_main.py"))
    assert os.path.exists(os.path.join(output_path, "src", "utils"))
    assert os.path.exists(os.path.join(output_path, "src", "utils", "helpers.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_helpers.py"))
    assert os.path.exists(os.path.join(output_path, "src", "services"))
    assert os.path.exists(os.path.join(output_path, "src", "services", "service.py"))
    assert os.path.exists(os.path.join(output_path, "tests", "test_service.py"))
    assert os.path.exists(os.path.join(output_path, "assets", "images"))
    assert os.path.exists(os.path.join(output_path, "data", "input"))
    assert os.path.exists(os.path.join(output_path, "data", "intermediate"))
    assert os.path.exists(os.path.join(output_path, "data", "output"))