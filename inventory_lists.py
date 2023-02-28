inventory_item_list = []
inventory_quantity_list = []

def add_new_item(new_item, number_available):
	"""
	Add a new item to the inventory with quantity number_available.
	Raises an exception if the item is already in the 
	inventory.
	"""
	if new_item in inventory_item_list:
		raise Exception('We already sell that.')
	inventory_item_list.append(new_item)
	inventory_quantity_list.append(number_available)

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
	print('Inventory:')
	for i in range(len(inventory_item_list)):
		print(f'\t{inventory_item_list[i]} - {inventory_quantity_list[i]}')

def main():
	print("***********HELLO CLASS**********")	

if __name__ == '__main__':
	main()