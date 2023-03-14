class Pair:

	def __init__(self, x, y):		
		self.x = x
		self.y = y	
				
	def sum(self):
		return self.x + self.y

	def multiply(self):
		return self.x * self.y

# instantiate an object of type Pair
even = Pair(2, 4)
odd = Pair(1, 3)

# call sum and print result
result = even.sum()
print(result)

result = odd.sum()
print(result)


def open_file(filename):
	file = open(filename)

def print_success(filename):
	open_file(filename)
	print('File open was successful')

def get_file_name():

	filename = input('enter file name: ')
	success = False
	while not success:
		try:
			print_success(filename)
			success = True
		except:
			print('bad file name')
			filename = input('enter file name: ')

get_file_name()

def validation(one, two):
	# one -- negative integer
	# two -- positive float less than 1000

	# if either param is invalid
	#	raise Exception
	
	if not isinstance(one, int) or not isinstance(two, float):
		raise TypeError('invalid type')
	if one <= 0 or two >= 1000:
		raise ValueError('bad value')

	return one * two



def remove_x(string):

	if len(string) == 0:
		return string

	if string[0] == 'x':
		return 	remove_x(string[1:])	
	else: # string[0] is not an x
		# return remove_x(string[1:]) + string[0]
		return string[0] + remove_x(string[1:])

# print(remove_x('xabxc'))
# print(remove_x('abc'))
# print(remove_x('xxx'))
# print(remove_x(''))
# print(remove_x('axbxc'))
# print(remove_x('aXbXc'))


def print_string_backward(string):
	"""
	Implement a recursive function that takes as input a str and prints 
	the characters of the str *in reverse* one per line *without using a loop*. 
	"""
	# if len(string) == 1:
	# 	print(string)
	# 	return

	if len(string) == 0:
		return

	print_string_backward(string[1:])
	print(string[0])	

# print_string_backward('hello')


# def sum(n):
# 	if n == 1:
# 		return 1
# 	return n + sum(n-1)


# result = sum(10)

# print(result)