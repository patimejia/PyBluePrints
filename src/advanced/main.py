import os

PROJECT_NAME = 'advanced_project'

dirs = [
    os.path.join(PROJECT_NAME, 'src'),
    os.path.join(PROJECT_NAME, 'src', 'submodules'),
    os.path.join(PROJECT_NAME, 'tests'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules'),
    os.path.join(PROJECT_NAME, 'data'),
    os.path.join(PROJECT_NAME, 'data', 'input'),
    os.path.join(PROJECT_NAME, 'data', 'output'),
    os.path.join(PROJECT_NAME, 'docs'),
    os.path.join(PROJECT_NAME, 'docs', 'api'),
    os.path.join(PROJECT_NAME, 'docs', 'api', 'submodules'),
    os.path.join(PROJECT_NAME, 'docs', '_static'),
    os.path.join(PROJECT_NAME, 'scripts'),
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
    os.path.join(PROJECT_NAME, 'src', 'submodules', 'submodule2.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_main.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules', 'test_submodule1.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_submodules', 'test_submodule2.py'),
    os.path.join(PROJECT_NAME, 'data', 'input', 'input_file1.txt'),
    os.path.join(PROJECT_NAME, 'data', 'input', 'input_file2.csv'),
    os.path.join(PROJECT_NAME, 'data', 'output', 'output_file1.txt'),
    os.path.join(PROJECT_NAME, 'docs', 'conf.py'),
    os.path.join(PROJECT_NAME, 'docs', 'index.rst'),
    os.path.join(PROJECT_NAME, 'docs', 'api', 'main.rst'),
    os.path.join(PROJECT_NAME, 'docs', 'api', 'submodules', 'submodule1.rst'),
    os.path.join(PROJECT_NAME, 'docs', 'api', 'submodules', 'submodule2.rst'),
    os.path.join(PROJECT_NAME, 'docs', '_static', 'style.css'),
    os.path.join(PROJECT_NAME, 'scripts', 'script1.py'),
    os.path.join(PROJECT_NAME, 'scripts', 'script2.py'),
    os.path.join(PROJECT_NAME, 'setup.py'),
    os.path.join(PROJECT_NAME, 'requirements.txt'),
    os.path.join(PROJECT_NAME, '.gitignore'),
    os.path.join(PROJECT_NAME, 'LICENSE'),
    os.path.join(PROJECT_NAME, 'README.md'),
]

for d in dirs:
    os.makedirs(d)

for f in init_files:
    open(f, 'w').close()

for f in other_files:
    open(f, 'w').close()
