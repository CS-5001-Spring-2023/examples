# # # Strings are immutable!

string = "Hello world"
print(string)

# # There are a number of methods you can call
# # on a string
# # see: https://docs.python.org/3/library/stdtypes.html
string = string.replace("l", "^^^")

# # # What does the following display?
# # # Is this a trick question?
print(string) 

# # Accessing individual characters in a string
# # using the [] syntax
# # Remember, computer scientists always start at 0!
i = 0
while i < len(string):
	print(string[i])
	i += 1 # i = i + 2

# i = len(string)-1
# while i >= 0:
# 	print(string[i])
# 	i -= 1

# # # Accessing slices of a string using the [::] syntax
print(string[2:7])
print(string[5:2:-1])

# """
# Exercises
# """

# Write a function that will take as input a string 
# and will return the reverse of the string.
# Example: input_string = "timbers" output_string = "srebmit"
def reverse_string(input_string):

	output_string = ""
	i = len(input_string) - 1
	while i >= 0:
		output_string = output_string + input_string[i]
		i = i - 1
	return output_string

def main():
	print(reverse_string("cow"))
	string = "cow"
	string[0] = 'X' # NOT ALLOWED

main()

# A palindrome is a word that is the same forward and backward.
# Examples are 'madam' 'racecar' and 'deed'
# Write a function that will determine whether an input
# string is a palindrome. Return True if so and False if
# not.
# You may assume that the string does not contain spaces.


