class Animal:

	def __init__(self, name, number_of_legs, is_mammal, color, favorite_word):
		self.name = name
		self.number_of_legs = number_of_legs
		self.is_mammal = is_mammal
		self.color = color
		self.favorite_word = favorite_word

	def speak(self):
		print(self.favorite_word)

	def change_name(self, new_name):
		self.name = new_name

	def get_name(self):
		return self.name

	def __str__(self):
		return f'name: {self.name}\nfavorite word: {self.favorite_word}'


def make_dog():
	dog = Animal("Spot", 4, True, "Brown", "Bark")
	print(type(dog))
	print(dog)


def main():
	make_dog()

main()