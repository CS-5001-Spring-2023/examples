def first(value1, value2):
	"""
	Exercise 1
	Write a function called first that receives two parameter values and returns the one that comes first. In the case of two numeric values, it would return the smaller of the two. In the case of two strings, it would return the one that comes first lexicographically (e.g., first("cat", "dog") returns "cat")
	"""
	if value1 > value2: 
		return value2
	else:
		return value1		


def get_animal_and_sound():
	response = input("Give me an animal and a sound\n")
	# "cat meow"
	return response.split()

def main():
	animal, sound = get_animal_and_sound()
	print(animal)
	print(sound)


main()



	# """
	# Exercise 2
	# Write a program (remember that programs have a main() function) to print the lyrics of the song "Old MacDonald." Your program should print the lyrics for five different animals (five verses), similar to the example verse below:

	# Old MacDonald had a farm, ee-igh, ee-igh, oh!
	# And on that farm he had a cow, ee-igh, ee-igh, oh!
	# With a moo, moo here and a moo, moo there.
	# Here a moo, there a moo, everywhere a moo, moo.
	# Old MacDonald had a farm, ee-igh, ee-igh, oh!

	# Remember not to duplicate code!
	# """