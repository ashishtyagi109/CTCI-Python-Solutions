from stack import *

class SetOfStacks(object):
	def __init__(self, capacity):
		self._capacity = capacity
		self._stacks = []
		self._stacks.append(Stack())

	def push(self, value):
		if (self._stacks[-1].size == self._capacity):
			self._stacks.append(Stack())
		self._stacks[-1].push(value)

	def pop(self):
		if (self._stacks[-1].isEmpty()):
			if (len(self._stacks) == 1):
				raise EmptyStackError()
			else:
				self._stacks.pop(-1)

		self._stacks[-1].pop()

	def peek(self):
		if (self._stacks[-1].isEmpty()):
			if (len(self._stacks) == 1):
				raise EmptyStackError()
			else:
				self._stacks.pop(-1)

		return self._stacks[-1].peek()

	def popAt(self, stackIndex):
		self._stacks[stackIndex].pop()
