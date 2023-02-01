# # for loops!

list = ["hello", "there", "cs", "5001", "class"]

# # # here is how we use while to iterate over a list
i = 0
while i < len(list):
	print(list[i])
	i += 1

# # here is one way using for loops!
for string in list:
	print(string)

# # but, sometimes we need the index
for index in range(len(list)):
	# print(i+1)
	print(f"{index+1} ### {list[index]}")

# Write a function that takes as input a positive integer 
# and uses a for loop to print the multiples of 5 that are 
# less than or equal to the number that was entered.

VOWELS = ['a', 'e', 'i', 'o', 'u']

# Write a function called count_vowels that takes a string 
# as an input and returns the number of vowels (a, e, i, o, u) 
# that are found in the sentence.
def count_vowels(sentence):
	count = 0
	# for letter in sentence:
	# 	# if (letter == 'a'
	# 	# 	or letter == 'e'
	# 	# 	or letter == 'i'
	# 	# 	or letter == 'o'
	# 	# 	or letter == 'u'
	# 	# 	):
	# 	if letter in VOWELS:
	# 		count += 1
	i = 0
	while i < len(sentence):
		# letter = sentence[i]
		if sentence[i] in VOWELS:
			count += 1
		i += 1

	return count

sentence = "hello world"
print(count_vowels(sentence))

sentence = "plrkms"
print(count_vowels(sentence))

sentence = "ouiae"
print(count_vowels(sentence))

sentence = ""
print(count_vowels(sentence))



