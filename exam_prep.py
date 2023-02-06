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
	pass


def main():
	# test average_grade
	grades = [
				[90, 95, 85],
				[80, 80, 80, 80],
				[90, 95, 100]
			]
	print(average_grade(grades))

	# print(average_grade(grades)) # should print 90, 80, 95



	# print(count_between("aa-c-a", "-")) # should return 1
	# print(count_between("aa-ccc-a-b", "-")) # should return 3
	# print(count_between("aa---a", "-")) # should return 0
	# print(count_between("aa-", "-")) # should return 0


main()

