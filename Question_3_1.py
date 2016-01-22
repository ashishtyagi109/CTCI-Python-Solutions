NUMBER_OF_STACKS = 3

class StackFullError(Exception):
	pass

class EmptyStackError(Exception):
	pass

class FixedSizeMultiStack(object):

	def __init__(self, stackSize):
		self._values = [None] *(stackSize*NUMBER_OF_STACKS)
		self._capacity = stackSize
		self._sizes = [0] * NUMBER_OF_STACKS

	def push(self, stackNumber, value):
		if (self._sizes[stackNumber] >= self._capacity):
			raise StackFullError(stackNumber)

		offset = (self._capacity) * stackNumber
		size = self._sizes[stackNumber]
		self._values[offset + size] = value
		self._sizes[stackNumber] += 1

	def peek(self, stackNumber):
		if(self.isEmpty(stackNumber)):
			raise EmptyStackError(stackNumber)

		offset = (self._capacity) * stackNumber
		size = self._sizes[stackNumber]
		return self._values[offset + size - 1]

	def pop(self, stackNumber):
		if(self.isEmpty(stackNumber)):
			raise EmptyStackError(stackNumber)

		offset = (self._capacity) * stackNumber
		size = self._sizes[stackNumber]
		self._values[offset + size - 1] = None # Remove value
		self._sizes[stackNumber] -= 1 # Reduce size

	def isEmpty(self, stackNumber):
		return (self._sizes[stackNumber] == 0)
