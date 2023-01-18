def main():
	
	# # Exercise 1
	# print("\nExercise 1")
	# print("="*10)
	# number = 10
	# if(number < 10):
	# 	print("Number is small.")
	# else:
	# 	print("Number is not small.")


	# # Exercise 2
	# print("\nExercise 2")
	# print("="*10)
	# number = 10
	# if(number > 15):
	# 	print("Seems like a big number.")
	# 	print("Are you sure that's right?")
	# else:
	# 	print("Good job! \n\"\\You picked a good number.")
	# 	# print("")

	# # Exercise 3
	# print("\nExercise 3")
	# print("="*10)
	# animal = "cat"
	# if(animal == "dog"):
	# 	print("woof")
	# elif(animal == "cow"):
	# 	print("moo")
	# elif(animal == "bird"):
	# 	print("meow")

	# Exercise 4
	print("\nExercise 4")
	print("="*10)
	first_name = "Sonny"
	last_name = "Rollins"
	if(first_name == "Sami" and last_name == "Rollins"):
		print("Hey, that's my name!")
	else:
		if(first_name == "Sami"):
			print("Cool first name haha")
		elif(last_name == "Rollins"):
			print("Cool last name")

	# Exercise 5
	print("\nExercise 5")
	print("="*10)	
	user_choice = "rock"
	if(user_choice != "rock" 
		and user_choice != "paper"
		and user_choice != "scissors"):
		print("Invalid chioce")
		print("Try again")
	else:
		print("Valid choice")


	# Exercise 6
	print("\nExercise 6")
	print("="*10)
	user_choice = "rock"
	if(not(user_choice == "rock" 
		or user_choice == "paper" 
		or user_choice == "scissors")):
		print("Invalid chioce")
		print("Try again")
	else:
		print("Valid choice")



	score = 87
	# grade = ""
	if(score > 90):
		grade = "A"
	elif(score > 80):
		grade = "B"
	elif(score > 70):
		grade = "C"
	print(f"A score of {score} earns a grade of {grade}.")


main()