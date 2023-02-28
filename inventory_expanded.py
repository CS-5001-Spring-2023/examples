import constants

inventory_number = 0

inventory = {}

def next_inventory_number():
	global inventory_number #Hey! We haven't learned about this.
	inventory_number = inventory_number + 1
	return inventory_number

def add_new_item(new_item, number_available):
	if new_item in inventory:
		raise Exception('We already sell that.')

	# Hey! We haven't learned about this either.
	item_info = dict(quantity = number_available,  inventory_number = next_inventory_number())

	"""
	# The following three lines are equivalent to the line above.
	item_info = {}
	item_info[constants.QUANTITY] = number_available
	item_info[constants.INVENTORY_NUMBER] = next_inventory_number()
	"""

	inventory[new_item] = item_info

def get_number_available(item_to_find):
	return inventory[item_to_find][constants.QUANTITY]

def update_number_available(item_to_find, number_purchased):
	item_info = inventory[item_to_find]
	available = item_info[constants.QUANTITY]
	if available >= number_purchased:
		item_info[constants.QUANTITY] = available - number_purchased
	else:
		raise Exception('Insufficent quantity.')

def show_inventory():
	print('Inventory:')
	for item in inventory:
		item_info = inventory[item]
		quantity = item_info[constants.QUANTITY]
		print(f'\t{item} - {quantity}')

def main():
	print(next_inventory_number())
	add_new_item('test', 12)
	show_inventory()

if __name__ == '__main__':
	main()