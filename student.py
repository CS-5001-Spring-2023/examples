class Student:

	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.scores = []

	def change_first_name(self, first):
		self.first = first

	def add_score(self, new_score):
		self.scores.append(new_score)

	def average_grade(self):
		total = 0
		for score in self.scores:
			total += score
		return total/len(self.scores)

	def __str__(self):
		# TODO: also include scores?
		return f'{self.first} {self.last}'

	def debug(self):
		print(f'{self.first} {self.last}')
		print(f'\t{self.scores}')
