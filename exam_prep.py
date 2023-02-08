def check_wordle_guess(wordle, guess):
	"""
	Write a function called check_wordle_guess that takes as 
	input two strings -- a wordle word and a user guess at 
	the wordle word. Return the number of characters that match, 
	i.e., would be colored green in the wordle game. Return -1 
	if the words are not the same length. 
	"""
	if len(wordle) != len(guess):
		return -1

	count = 0
	for i in range(len(wordle)):
		if wordle[i] == guess[i]:
			count = count + 1
	return count


# An example to iterate over two lists
names = ["juan", "hiromi", "susan"]
dates = [1992, 2003, 2001]

if len(names) != len(dates):
	exit() #Or, error

for i in range(len(names)):
	print(f"{i+1}: {names[i]} -- {dates[i]}")	

# An example of three loops to iterate over a list.
list = ["juan", "hiromi", "susan"]
i = 0
while i < len(list):
	print(list[i])
	i = i + 1

for i in range(len(list)):
	print(f"Item {i+1} is {list[i]}")

for character in list:
	print(character)



def average_grade(grades):
	"""
	Write a function that will take as input a two dimensional list of floats where each 
	sub-list represents the grades for a given student. Return a list of average grades
	for each student.
	Parameters:
		grades : list of lists of floats
	Returns:
		list of floats
	"""
	# result = []
	print(f"Number of students represented is {len(grades)}.")
	for student in grades:
		# type of student is list
		# student = [90, 95, 85]
		
		result = []	
		print(f"Number of individual scores for this student is {len(student)}.")

		total = 0
		for score in student:
			total = total + score
		average = total/len(student)
		result.append(average)
	return result


def count_between(word, delimiter):
	"""
	Write a function that takes as input a word and a delimiter character. Return 
	the number of non-delimiter characters that appear between the first two instances
	of the delimiter. If there is no ending delimiter return 0.
	Examples: 
		word = 'aa-c-a'; delimiter = '-'; result = 1
		word = 'aa-ccc-a-b'; delimiter = '-'; result = 3
		word = 'aa---a'; delimiter = '-'; result = 0
		word = 'aa-'; delimiter = '-'; result = 0
	"""
	'''
	for each char of the word
		if char is not the delim and i've never seen the delim
			continue
		if char is the delim and i've never seen the delim
			new state is delim
		if char is not the delim and i've seen the delim
			increment count
		if char is the delim and i've seen the delim
			new state is no delim
			return the count
	special cases...

	'''
	# if there are fewer than 2 delimiters
	# 	return 0


	count = 0
	delimiter_seen = False
	for character in word:
	# for i in range(len(word)):
		# character = word[i]


		if character == delimiter and not delimiter_seen:
			delimiter_seen = True
		elif character != delimiter and delimiter_seen:
			count += 1
		elif character == delimiter and delimiter_seen:
			delimiter_seen = False
			return count
	
	# # TODO: special cases -- "-aaaa"
	# if delimiter_seen:
	# 	return 0
	return count



def find_word_in_file(word, filename):	
	"""
	Searches for a given word in a file. 
	Parameters:
	word: str
		the search term
	filename: str
		the name of the file to search
	Returns:
	list
		line numbers where word appears in filename
	"""
	pass


def is_valid_command(command):
	result = command.split(" ")
	if len(result) != 2:
		return False
	if not result[1].isdigit():
		return False
	return True

def loop_example():

	command = input("What is your command: ")
	while command != "quit":
		if is_valid_command(command):
			char, iterations = command.split(" ")
			iterations = int(iterations)
			print(f'char = {char}')
			print(f'iterations = {iterations}') 

			for i in range(iterations):
				print(char, end = " ")
			print("\n")
		command = input("What is your command: ")


def main():
	# test average_grade
	# grades = [
	# 			[90, 95, 85],
	# 			[80, 80, 80, 80],
	# 			[90, 95, 100]
	# 		]
	# print(average_grade(grades))

	# print(find_word_in_file("fish", "text_file.txt"))


	print(count_between("aa-c-a", "-")) # should return 1
	print(count_between("aa-ccc-a-b", "-")) # should return 3
	print(count_between("aa---a", "-")) # should return 0
	print(count_between("aa-", "-")) # should
	print(count_between("-aaaaa", "-")) # should

	# loop_example()



main()

