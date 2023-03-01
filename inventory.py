from inventory_item import Inventory_Item

class Inventory:

	def __init__(self):
		self.inventory = {}

	def add_new_item(self, new_item, number_available):
		# TODO: verify item is not already in inventory
		new_inventory_item = Inventory_Item(new_item, number_available)
		self.inventory[new_item] = new_inventory_item

	def update_number_available(self, item_to_find, number_purchased):
		pass

	def show_inventory(self):
		print('Inventory:')
		for item in self.inventory:
			print(self.inventory[item])


inventory = Inventory()
inventory.add_new_item('Cake', 12)
inventory.add_new_item('Scone', 6)
inventory.show_inventory()




