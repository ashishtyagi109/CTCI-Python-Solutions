class EmptyStackError(Exception):
	pass		

class Stack(object):

	def __init__(self):
		self._stack = []

	def push(self, value):
		self._stack.append(value)

	def pop(self):
		if (self.isEmpty()):
			raise EmptyStackError("Can't pop")
		self._stack.pop(-1)

	def peek(self):
		if (self.isEmpty()):
			raise EmptyStackError("Can't peek")
		return self._stack[-1]

	def isEmpty(self):
		return (len(self._stack) == 0)


		