from inventory_item import InventoryItem
import unittest

class InventoryItemTest(unittest.TestCase):

	def test_call_to_constructor(self):
		item1 = InventoryItem('Brownies', 12)
		self.assertEqual(item1.quantity, 12)
		self.assertEqual(item1.name, 'Brownies')

	def test_purchase(self):
		item1 = InventoryItem('Brownies', 12)
		result = item1.purchase(2)
		self.assertEqual(item1.quantity, 10)

	def test_unsuccessful_purchase(self):
		item1 = InventoryItem('Brownies', 12)
		result = item1.purchase(20)
		self.assertFalse(result)

	def test_successful_purchase(self):
		item1 = InventoryItem('Brownies', 12)
		result = item1.purchase(2)
		self.assertTrue(result)


def main():
	unittest.main()

if __name__ == '__main__':
	main()