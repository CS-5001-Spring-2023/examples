class Stack:

	def __init__(self, init_size):
		self.max_size = init_size
		self.items = []

	def push(self, item):
		if len(self.items) >= self.max_size:
			raise Exception('stack full')
		self.items.append(item)

	def pop(self):
		if len(self.items) == 0:
			raise Exception('stack empty')
		item = self.items.pop()
		return item

	def size(self):
		return len(self.items)

	def debug(self):
		print(self.items)
