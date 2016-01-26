from stack import *

class EmptyQueueError(Exception):
	pass
		

class QueueWithStacks(object):

	def __init__(self):
		self._pushStack = Stack()
		self._popStack = Stack()

	def push(self, value):
		self._pushStack.push(value)

	def dequeue(self):
		if (self.isEmpty()):
			raise EmptyQueueError("Can't pop")

		if (self._popStack.isEmpty()):
			while (not self._pushStack.isEmpty()):
				temp = self._pushStack.peek()
				self._pushStack.pop()
				self._popStack.push(temp)

		self._popStack.pop()

	def peek(self):
		if (self.isEmpty()):
			raise EmptyQueueError("Can't peek")

		if (self._popStack.isEmpty()):
			while (not self._pushStack.isEmpty()):
				temp = self._pushStack.peek()
				self._pushStack.pop()
				self._popStack.push(temp)

		return self._popStack.peek()		 

	def isEmpty(self):
		return (self._pushStack.isEmpty() and self._popStack.isEmpty())
