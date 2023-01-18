"""
Use functions to implement a guessing game.
The game will randomly select a number 
between 1 and 10.
It will then ask the user to guess the number.
If the user guesses correctly, a "You won!" 
message will be displayed.
If the user guesses incorrectly, a "Try again!" 
message will be displayed.
"""
from random import randint


# function takes no input parameters
def get_computer_choice():
	
	# generate a random number
	value = randint(1, 10)
	
	# return that random number
	return value

# function takes no input parameters
def get_user_choice():
	
	# get choice from user
	value = int(input("What is your choice? (number 1-10) - "))

	# return the user's choice
	return value
	

#function takes two parameters
# -- user_choice and computer_choice
def user_wins(user_choice, computer_choice):
	# returns true if numbers are the same and false otherwise
	
	if(user_choice == computer_choice):
		return True
	else:
		return False

	# elif(user_choice != computer_choice):
	# return (user_choice == computer_choice)

# function takes two inputs
# -- user_choice, computer_choice
def declare_winner(user_choice, computer_choice):
	# prints the final result
	result = user_wins(user_choice, computer_choice)
	if(result):
		print("User has won!")
	else:
		print("Computer has won")


def main():
	# Computer chooses a number
	computer_choice = get_computer_choice()
	print(f"Computer chose {computer_choice}")

	# Ask user for number
	user_choice = get_user_choice()
	print(f"You chose {user_choice}")

	# # Compare numbers
	# result = user_wins(user_choice, computer_choice)
	# decided to change design -- compare numbers from 
	# within declare_winner function

	# Declare win/loss
	declare_winner(user_choice, computer_choice)

main()

