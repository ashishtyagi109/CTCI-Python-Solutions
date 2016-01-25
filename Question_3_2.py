from stack import *

class StackWithMin(Stack):

	def __init__(self):
		super(StackWithMin, self).__init__()
		self._minStack = []


	def push(self, value):
		super(StackWithMin, self).push(value)
		if (not self._minStack): # minStack is empty
			self._minStack.append(value)
		else:
			if (value <= self._minStack[-1]):
				self._minStack.append(value)

	def pop(self):
		poppedValue = super(StackWithMin, self).peek()
		super(StackWithMin, self).pop()

		if (poppedValue == self._minStack[-1]):
			self._minStack.pop(-1)

	def min(self):
		if (super(StackWithMin,self).isEmpty()):
			raise EmptyStackError
		return self._minStack[-1]
