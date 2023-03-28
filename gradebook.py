from student import Student

class Gradebook:

	def __init__(self):
		self.students = []

	def average_class_score(self):
		total = 0
		for student in self.students:
			total += student.average_grade()
		return total/len(self.students)

	def add_student(self, first, last):
		student = Student(first, last)
		self.students.append(student)

	def add_score(self, first, last, score):
		# TODO: return T/F if successful		
		for student in self.students:
			if student.first == first and student.last == last:
				student.add_score(score)
				break

	def debug(self):
		for student in self.students:
			student.debug()	