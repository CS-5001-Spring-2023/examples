def factorial_iterative(n):
	"""
	Implement a function `def factorial(n):` in Python. The function takes as input an
	integer and returns the factorial of that number.
	"""
	factorial = 1
	current_value = 1
	while current_value <= n:
		factorial = factorial * current_value
		current_value += 1
	return factorial

def factorial_recursive(n):
	"""
	Implement a function `def factorial(n):` in Python. The function takes as input an
	integer and returns the factorial of that number.
	Do not use a loop in the implementation of this function.
	"""	
	if n == 1:
		return 1
	# return n * factorial_recursive(n-1)

	result = factorial_recursive(n-1)
	my_value = n * result
	return my_value

# print(factorial_recursive(5))	


def print_string(string):
	"""
	Implement a recursive function that takes as input a str and prints 
	the characters of the str one per line *without using a loop*. 
	"""
	# base case
	print(f"my string is {string}")
	if len(string) == 0:
		print("returning...")
		return

	# do the job
	print(string[0])

	# recurse -- making the string smaller
	print_string(string[1:])

# print_string("bird")

def print_string_backward(string):
	"""
	Implement a recursive function that takes as input a str and prints 
	the characters of the str *in reverse* one per line *without using a loop*. 
	"""
	if len(string) == 0:
		return

	# print(string[0])
	print_string_backward(string[1:])
	print(string[0])

# print_string_backward("bird")

def print_nums_iterative(n):
	"""
	A function that takes as input a number and prints from 1 to 
	the number (inclusive).
	"""
	number = 1
	while number <= n:
		print(number)
		number += 1


def print_nums_recursive(n):
	"""
	Implement print_nums_iterative above without using a loop.
	"""
	# print_nums_recursive_helper(1, n)
	if n == 1:
		print(n)
		return

	print_nums_recursive(n-1)
	print(n)


print_nums_recursive(5)

# 1, 5
def print_nums_recursive_helper(current, n):
	if current == n:
		print(n) # or print(current)
		return
	
	print(current)
	print_nums_recursive_helper(current+1, n)



def find_char_a(string):
	"""
	Implement a function that returns the number of times the 
	character "a" appears in a str without using a loop. You 
	may not take a slice of the string, and you may only access 
	a single character of the string in any iteration of the 
	function.
	"""
	pass

def find_char_a_helper(string, current_position):
	pass


def in_english(number):
	"""
	Write a recursive function called in_english that takes a 
	integer value as input and returns a string containing 
	the digits of the number in English. For example, 
	in_english(153) would return "one five three".
	"""
	pass

def binarysearch(list, target):
 	"""
 	Write a recursive function that returns True if the target
 	exisits in the list and False otherwise.
 	"""
 	if len(list) < 2:
 		# we're a little bit cheating here
 		return target in list 
 	mid = len(list) // 2
 	if list[mid] == target:
 		return True
 	if target < list[mid]:
 		return binarysearch(list[:mid], target)
 	return binarysearch(list[mid+1:], target)

print(binarysearch([1, 3, 45, 67, 89], 45))
print(binarysearch([1, 3, 45, 67, 89], 1))
print(binarysearch([1, 3, 45, 67, 89], 3))
print(binarysearch([1, 3, 45, 67, 89], 67))
print(binarysearch([1, 3, 45, 67, 89], 89))
print(binarysearch([1, 3, 45, 67, 89], -2))
print(binarysearch([1, 3, 45, 67, 89], 18))
print(binarysearch([1, 3, 45, 67, 89], 92))
print(binarysearch([1, 3, 45, 67, 89, 92], 92))
print(binarysearch([1, 3, 45, 67, 89, 92], 93))
print(binarysearch([1, 3, 45, 67, 89, 92], 0))