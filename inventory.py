from inventory_item import InventoryItem

class Inventory:

	def __init__(self):
		self.inventory = {}

	def add_new_item(self, new_item, number_available):
		# TODO: verify item is not already in inventory		
		new_inventory_item = InventoryItem(new_item, number_available)
		self.inventory[new_item] = new_inventory_item

	def update_number_available(self, item_to_find, number_purchased):
		pass

	def show_inventory(self):
		print('Inventory:')
		for item in self.inventory:
			print(self.inventory[item])

