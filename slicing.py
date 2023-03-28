from student import Student

student1 = Student('Joe', 'Rollins')
student2 = Student('Suzy', 'Smith')
student3 = Student('Pari', 'Goetz')
student4 = Student('Hiromi', 'Hiraoka')
student5 = Student('Nate', 'Derbinsky')
student6 = Student('Alan', 'Mislove')


list1 = []
list1.append(student1)
list1.append(student2)
list1.append(student3)
list1.append(student4)
list1.append(student5)
list1.append(student6)
list2 = list1[2:5]

list1[4]
list2[2]
student5


student3.change_first_name('Parisima')

print('LIST 1')
for student in list1:
	print(student)
print('='*10)
print('LIST 2')
for student in list2:
	print(student)
print('='*10)
list1[4].change_first_name('Nathaniel')
print('LIST 1')
for student in list1:
	print(student)
print('='*10)
print('LIST 2')
for student in list2:
	print(student)


