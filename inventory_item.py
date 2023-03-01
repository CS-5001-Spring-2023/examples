class Inventory_Item:

	# inventory_number_generator = 1

	def __init__(self, name, quantity):
		self.name = name
		self.quantity = quantity
		self.inventory_number = 'a123f'

	def __str__(self):
		return f'\t{self.name} - {self.quantity}'

	def purchase(self, num_to_purchase):
		self.quantity -= num_to_purchase

	def get_number_available(self):
		return self.quantity
