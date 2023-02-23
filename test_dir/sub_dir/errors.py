import os

# See: https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/os.html


def convert(value, target_type):
	"""
	Write a function to convert value into the target type. 
	Valid type for target_type is int or float.
	"""
	pass

def read_file(filename):
	"""
	Write a function to display the contents of a file.
	The function will throw an exception if the file is
	not found.
	"""
	pass


def find_py_files(root):
	"""
	Write a recursive function to list all files 
	in any descendant directory of a given root.
	"""
	# os.path.isfile(FILENAME) -- boolean T if this is a file
	# os.path.isdir(NAME) -- boolean T if this is a directory

	if os.path.isdir(root):
		results = os.listdir(root)
		for result in results:
			find_py_files(os.path.join(root, result))
	elif os.path.isfile(root) and root.endswith(".py"):
		print(f"Python file: {root}")

def main():
	find_py_files('/Users/srollins/teaching/cs5001-s23/examples')
	

main()



