from student import Student
from gradebook import Gradebook

gradebook = Gradebook()

first = 'Joe'
last = 'Rollins'
gradebook.add_student(first, last)

first = 'Pari'
last = 'Goetz'
gradebook.add_student(first, last)

first = 'Nate'
last = 'Derbinsky'
gradebook.add_student(first, last)


first = 'Nate'
last = 'Derbinsky'
score = 90
gradebook.add_score(first, last, score)
score = 90
gradebook.add_score(first, last, score)
score = 90
gradebook.add_score(first, last, score)
score = 90
gradebook.add_score(first, last, score)

first = 'Joe'
last = 'Rollins'
score = 100
gradebook.add_score(first, last, score)
score = 100
gradebook.add_score(first, last, score)
score = 100
gradebook.add_score(first, last, score)
score = 100
gradebook.add_score(first, last, score)

first = 'Pari'
last = 'Goetz'
score = 95
gradebook.add_score(first, last, score)
score = 95
gradebook.add_score(first, last, score)
score = 95
gradebook.add_score(first, last, score)
score = 95
gradebook.add_score(first, last, score)


gradebook.debug()
print(gradebook.average_class_score())