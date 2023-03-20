from stack import Stack
import unittest

class StackTest(unittest.TestCase):

	def test_push_pop_simple(self):
		stack = Stack(5)
		stack.push(1)
		result = stack.pop()
		self.assertEqual(result, 1)

	def test_push_pop_complex(self):
		stack = Stack(5)
		stack.push(1)
		stack.push(2)
		result = stack.pop()
		stack.push(3)
		result = stack.pop()
		self.assertEqual(result, 3)
		
	def test_push_full(self):
		stack = Stack(2)
		stack.push(1)
		stack.push(2)
		self.assertRaises(Exception, stack.push, 3)

	def test_pop_empty(self):
		stack = Stack(2)
		self.assertRaises(Exception, stack.pop)

	def test_size(self):
		stack = Stack(2)
		stack.push(1)
		result = stack.size()
		self.assertEqual(result, 1)

def main():
	unittest.main()

if __name__ == '__main__':
	main()

