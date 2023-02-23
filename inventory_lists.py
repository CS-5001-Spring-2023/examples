inventory_item_list = ['Chocolate Brownie', 'Carrot Cake', 'Blueberry Scone']
inventory_quantity_list = [12, 5, 9]

def get_number_available(item_to_find):
	"""
	Return the number of the given item that are available
	in the inventory.
	Raises a KeyError if the item is not found in the inventory.
	"""
	for i in range(len(inventory_item_list)):
		if inventory_item_list[i] == item_to_find:			
			return inventory_quantity_list[i]
	raise KeyError(f'Key {item_to_find} not found.')

def update_number_available(item_to_find, number_purchased):	
	"""
	Update the number of the given item that are available in 
	the inventory.
	Raises an Exception if there is not a sufficient quantity 
	of the item available. 
	"""
	for i in range(len(inventory_item_list)):
		if inventory_item_list[i] == item_to_find:		
			if inventory_quantity_list[i] >= number_purchased:
				inventory_quantity_list[i] -= number_purchased
			else:
				raise Exception('Insufficent quantity.')

def show_inventory():
	"""
	Display the item names and amounts for all items in the
	inventory.
	"""
	for i in range(len(inventory_item_list)):
		print(f'There are {inventory_quantity_list[i]} {inventory_item_list[i]} available.')
