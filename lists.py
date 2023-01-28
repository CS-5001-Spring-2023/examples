# Lists are mutable

# a list of strings
string_list = ['hello', 'world']

# a list of ints 
int_list = [93, 56, 23]

# a list of mixed types
# but don't do this!
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
	string = "NEW STRING"

def changelist(list):
	list[0] = 999

print(int_list)
changelist(int_list)
print(int_list)
string = "hello"
print(string)
changestring(string)
print(string)

"""
Exercises
"""

# Write a function that takes a list of strings
# and combines them into a single string with 
# spaces between each word. 
# The input will be the list and the output
# will be the final string.

# Write a function that takes as input a list
# of ints and returns the number of values
# in the list greater than 100.

