# for loops!

list = ["hello", "there", "cs", "5001", "class"]

# here is how we use while to iterate over a list
i = 0
while i < len(list):
	print(list[i])
	i += 1

# here is one way using for loops!
for string in list:
	print(string)

# but, sometimes we need the index
for i in range(len(list)):
	print(f"{i}: {list[i]}")

# Write a function that takes as input a positive integer 
# and uses a for loop to print the multiples of 5 that are 
# less than or equal to the number that was entered.

# Write a function called count_vowels that takes a string 
# as an input and returns the number of vowels (a, e, i, o, u) 
# that are found in the sentence.
