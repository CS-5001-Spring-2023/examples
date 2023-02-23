# import inventory_lists as inventory
# import inventory_dictionary as inventory
import inventory_expanded as inventory

def main():
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