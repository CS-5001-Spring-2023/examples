import os

# See: https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/library/os.html


def convert(value, target_type):
	"""
	Write a function to convert value into the target type. 
	Valid type for target_type is int or float.
	If the value is already the target_type
		return the value without conversion
	If the target_type is not int or float
		generate a TypeError
	If the value cannot be converted
		return a ValueError
	"""
	if isinstance(value, target_type):
		return value
	
	if target_type != int and target_type != float:
		raise TypeError(f"Cannot convert to type {target_type}.")

	if target_type == int:
		int_value = int(value)
		return int_value
	
	if target_type == float:
		float_value = float(value)
		return float_value


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

	# results = os.walk(root)
	# for result in results:
	# 	print(result)

	if os.path.isfile(root) and root.endswith(".py"):
		print(f"Python file: {root}")

	elif os.path.isdir(root):
		results = os.listdir(root)
		for result in results:
			find_py_files(os.path.join(root, result))
 
def main():
	# find_py_files('/Users/srollins/teaching/cs5001-s23/examples')

	result = convert("3", int)	
	print(result)
	result = convert("3.3", float)	
	print(result)

	try:

		result = convert(3, str) # TypeError
		print(result)
			
		result = convert("cow", float) # ValueError
		print(result)
		
	except ValueError as ex:
		print('value error', ex)
	except TypeError as ex:
		print('type error', ex)

	print('done')
	

main()



