
inventory = {}

def add_new_item(new_item, number_available):
	if new_item in inventory:
		raise Exception('We already sell that.')
	inventory[new_item] = number_available

def get_number_available(item_to_find):
	return inventory[item_to_find]

def update_number_available(item_to_find, number_purchased):

	available = inventory[item_to_find]
	if available >= number_purchased:
		inventory[item_to_find] = available - number_purchased
	else:
		raise Exception('Insufficent quantity.')
	
def show_inventory():
	print('Inventory:')
	for item in inventory:
		print(f'\t{item} - {inventory[item]}')

def main():
	show_inventory()
	# print(inventory['Carrot Cake'])
	# inventory['Biscuit'] = 20
	# print(inventory['Biscuit'])
	# inventory['Biscuit'] = 4000
	# print(inventory['Biscuit'])
	add_new_item('Carrot Cake', 5)
	add_new_item('Chocolate Brownie', 12)
	show_inventory()

if __name__ == '__main__':
	main()