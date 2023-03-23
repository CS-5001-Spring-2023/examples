from stack import Stack

open_chars = ['(', '{', '[']
close_chars = [')', '}', ']']

def is_open(char):
	return char in open_chars

def is_close(char):
	return char in close_chars

def match(open_char, close_char):
	if open_char not in open_chars or close_char not in close_chars:
		return False
		
	if open_chars.index(open_char) == close_chars.index(close_char):
		return True
	return False

	# if open_char == '(' and close_char == ')':
	# 	return True
	# if open_char == '{' and close_char == '}':
	# 	return True
	# if open_char == '[' and close_char == ']':
	# 	return True
	# return False

def check(paren_string):
	parens = Stack(10)

	for close_char in paren_string:	
		if is_open(close_char):
			parens.push(close_char)
		elif is_close(close_char):
			if parens.size() == 0:
				return False
			open_char = parens.pop()
			if not match(open_char, close_char):
				return False				
	if parens.size() > 0:
		return False
	return True


# paren_string = '(()())'
# result = check(paren_string)
# print(result, paren_string)
