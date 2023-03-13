class InventoryItem:

	inventory_number_generator = 1

	def __init__(self, name, quantity):
		self.name = name
		self.quantity = quantity
		self.num_sold = 0
		self.inventory_number = InventoryItem.inventory_number_generator
		InventoryItem.inventory_number_generator += 1

	def __str__(self):
		return f'\t{self.name} - {self.quantity} - {self.inventory_number}'

	def purchase(self, num_to_purchase):
		success = True
		if num_to_purchase > self.quantity:
			success = False
		else:
			self.quantity -= num_to_purchase
			self.num_sold += num_to_purchase

		return success

	def get_number_available(self):
		return self.quantity











