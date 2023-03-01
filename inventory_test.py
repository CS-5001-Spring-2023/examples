# import inventory_lists as inventory
# import inventory_dictionary as inventory
# import inventory_expanded as inventory
# from inventory import Inventory
# from inventory_item import Inventory_Item

def main():

	inventory.show_inventory()
	print('='*10)

	inventory.add_new_item('Chocolate Brownie', 12)
	inventory.add_new_item('Carrot Cake', 5)
	inventory.add_new_item('Blueberry Scone', 9)

	try:
		inventory.add_new_item('Carrot Cake', 5)
	except:
		print('Carrot Cake already in the inventory.')

	inventory.show_inventory()
	print('='*10)

	number_to_buy = 3
	item = 'Blueberry Scone'
	print(f'Buying {number_to_buy} {item}.')
	print('='*10)
	inventory.update_number_available(item, number_to_buy)
	
	inventory.show_inventory()
	print('='*10)

if __name__ == '__main__':
	main()