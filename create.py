from os import path
from sys import argv
from re import sub

def create_files(dir, pname):
	root_dir = path.dirname(__file__)

	snake_case = camel_to_snake(pname)

	# Create test file
	with open(path.join(root_dir, dir, f'{pname}.py')) as f:
		f.write()
		

def camel_to_snake(name):
    name = sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


if __name__ == '__main__':
	pth = "/".join(argv[1:-1])
	pname = argv[-1]

	create_files(pth, pname)
	