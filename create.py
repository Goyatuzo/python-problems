from os import path, makedirs
from sys import argv
from re import sub
from shutil import copy

def create_files(dir, pname):
	root_dir = path.dirname(__file__)

	snake_case = camel_to_snake(pname)
	new_test_file = path.join(root_dir, dir)

	# Make files
	makedirs(new_test_file, exist_ok=True)
	create_file(path.join(root_dir, 'basic_files', 'basic_test.py'), path.join(new_test_file, f'{snake_case}_test.py'), snake_case)
	create_file(path.join(root_dir, 'basic_files', 'basic.py'), path.join(new_test_file, f'{snake_case}.py'), snake_case)
	

def create_file(template_file, new_file, problem_name):
	copy(template_file, new_file)

	with open(template_file, mode='r') as inp:
		with open(new_file, mode='w') as out:
			for line in inp:
				print(line)
				out.write(line.replace('basic', problem_name))

def camel_to_snake(name):
    name = sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


if __name__ == '__main__':
	pth = "/".join(argv[1:-1])
	pname = argv[-1]

	create_files(pth, pname)
	