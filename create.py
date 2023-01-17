from os import path, makedirs
from sys import argv
from re import sub
from shutil import copy

def create_files(dir, pname):
	root_dir = path.dirname(__file__)

	snake_case = camel_to_snake(pname)
	new_test_file = path.join(root_dir, dir)

	# Create test file
	makedirs(new_test_file, exist_ok=True)
	copy(path.join(root_dir, 'basic_files', 'basic_test.py'), path.join(new_test_file, f'{snake_case}.py'))
		

def camel_to_snake(name):
    name = sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


if __name__ == '__main__':
	pth = "/".join(argv[1:-1])
	pname = argv[-1]

	create_files(pth, pname)
	