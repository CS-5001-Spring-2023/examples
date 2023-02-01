# # # Lists are mutable

# # # a list of strings
string_list = ['hello', 'world']

# # # a list of ints 
int_list = [93, 56, 23]
print(int_list[0])

int_list[0] = 999
print(int_list[0])

# # # a list of mixed types
# # # but don't do this!
mixed_list = [3, "dog", "night"] 


# print a list from start to finish
i = 0
while i < len(string_list):
	print(string_list[i])
	i += 1

# Hey! Lists are mutable.
string_list[1] = "class"
string_list.append("Welcome!")
i = 0
while i < len(string_list):
	print(string_list[i])
	i += 1

# What is the output of the following fragment?
def changestring(string):
	print(string)
	string = "NEW STRING"
	print(string)

def changelist(list):
	list[0] = 99
	print(string_list[0])

int_list = [93, 56, 23]
print(int_list)
changelist(int_list)
print(int_list)
greeting = "hello"
print(greeting)
changestring(greeting)
print(greeting)

# """
# Exercises
# """

# Write a function that takes a list of strings
# and combines them into a single string with 
# spaces between each word. 
# The input will be the list and the output
# will be the final string.

# Write a function that takes as input a list
# of ints and returns the number of values
# in the list greater than 100.
def greater_than_100(int_list):
	count = 0
	for number in int_list:
		if number > 100:
			count += 1		
	return count


int_list = [93, 560, 23, 344, 1, 342, 2, 4232]
print(greater_than_100(int_list)) # expected 4

int_list = [93, 50, 23, 34, 1, 34, 2, 42]
print(greater_than_100(int_list)) # expected 0

int_list = []
print(greater_than_100(int_list)) # expected 0

int_list = [93, 100, 45.3]
print(greater_than_100(int_list)) # expected 0


int_list = [93, 100, 45.3, 923.6]
print(greater_than_100(int_list)) # expected 1
