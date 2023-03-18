import os

PROJECT_NAME = 'basic_project'

dirs = [
    os.path.join(PROJECT_NAME, 'src'),
    os.path.join(PROJECT_NAME, 'tests'),
]

files = [
    os.path.join(PROJECT_NAME, 'src', 'main.py'),
    os.path.join(PROJECT_NAME, 'tests', 'test_main.py'),
    os.path.join(PROJECT_NAME, 'README.md'),
]

for d in dirs:
    os.makedirs(d)

for f in files:
    open(f, 'w').close()
