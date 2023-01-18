

def welcome():
	"""
	Exercise 1:
	A function to print a multi-line welcome message.
	# example of how to print this documentation - print(welcome.__doc__)
	"""
	print("Hello lovely class.")
	print("Welcome to CS 5001")
	print("on this fine winter day.")

def greet_by_name(name):
	"""
	Exercise 2:
	A function to greet a user by name.
	Parameters
	name : str
		name of the user
	"""
	print(f"Hello, {name}!")

def get_greeting():
	"""
	Exercise 3:
	A function to get a specific greeting from the user.
	Returns:
	str
		name entered by the user
	"""
	greeting = input("How would you like to greet your user? ")
	return greeting


def welcome_by_name_with_greeting(name, greeting):
	"""
	Exercise 4:
	A function to welcome a user by name with a specific
	greeting.
	Parameters:
	name : str
		name of the user
	greeting : str
		greeting to use 	
	"""
	print(f"{greeting}, {name}")

def main():
	name = "Liz"
	greeting = get_greeting()
	welcome_by_name_with_greeting(name, greeting)

	name = "Ethan"
	welcome_by_name_with_greeting(name, get_greeting())

	name = "Timothy"
	welcome_by_name_with_greeting(name, greeting)


main()





