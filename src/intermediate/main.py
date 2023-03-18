import os

PROJECT_NAME = 'intermediate_project'

dirs = [
    os.path.join(PROJECT_NAME, 'src'),
    os.path.join(PROJECT_NAME, 'src', 'submodules'),
    os.path.join(PROJECT_NAME, 'tests'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules'),
    os.path.join(PROJECT_NAME, 'data'),
]

init_files = [
    os.path.join(PROJECT_NAME, 'src', '__init__.py'),
    os.path.join(PROJECT_NAME, 'src', 'submodules', '__init__.py'),
    os.path.join(PROJECT_NAME, 'tests', '__init__.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules', '__init__.py'),
]

other_files = [
    os.path.join(PROJECT_NAME, 'src', 'main.py'),
    os.path.join(PROJECT_NAME, 'src', 'submodules', 'submodule1.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_main.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules', 'test_submodule1.py'),
    os.path.join(PROJECT_NAME, 'data', 'input.txt'),
    os.path.join(PROJECT_NAME, 'data', 'output.txt'),
    os.path.join(PROJECT_NAME, 'README.md'),
]

for d in dirs:
    os.makedirs(d)

for f in init_files:
    open(f, 'w').close()

for f in other_files:
    open(f, 'w').close()
