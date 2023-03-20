import paren_checker
import unittest

class ParenCheckerTest(unittest.TestCase):

	def test_is_open_regular(self):
		self.assertTrue(paren_checker.is_open('('))
	
	def test_is_open_curly(self):
		self.assertTrue(paren_checker.is_open('{'))

	def test_is_open_square(self):
		self.assertTrue(paren_checker.is_open('['))

	def test_is_open_false(self):
		self.assertFalse(paren_checker.is_open(')'))

	def test_is_open_invalid(self):
		self.assertFalse(paren_checker.is_open('*'))

	def test_is_close_regular(self):
		self.assertTrue(paren_checker.is_close(')'))
	
	def test_is_close_curly(self):
		self.assertTrue(paren_checker.is_close('}'))

	def test_is_close_square(self):
		self.assertTrue(paren_checker.is_close(']'))

	def test_is_close_false(self):
		self.assertFalse(paren_checker.is_close('{'))

	def test_is_close_invalid(self):
		self.assertFalse(paren_checker.is_close('*'))

	def test_match_regular(self):
		self.assertTrue(paren_checker.match('(', ')'))

	def test_match_curly(self):
		self.assertTrue(paren_checker.match('{', '}'))

	def test_match_square(self):
		self.assertTrue(paren_checker.match('[', ']'))

	def test_match_false(self):
		self.assertFalse(paren_checker.match('(', '}'))

	def test_match_invalid(self):
		self.assertFalse(paren_checker.match('A', 'B'))

	def test_check_simple(self):
		self.assertTrue(paren_checker.check('(()())'))

	def test_check_simple_false(self):
		self.assertFalse(paren_checker.check('(()()'))

	def test_check_multitype(self):
		self.assertTrue(paren_checker.check('({}[])'))

	def test_check_complex(self):
		self.assertTrue(paren_checker.check('(({})[]([]))'))

	def test_check_multitype_false(self):
		self.assertFalse(paren_checker.check('({][])'))

	def test_check_complex_false(self):
		self.assertFalse(paren_checker.check('(({})[][[]))'))



def main():
	unittest.main()

if __name__ == '__main__':
	main()