from stack import *

class SortStack(Stack):

	def __init__(self):
		super(SortStack, self).__init__()

	def sort(self):
		buffer = Stack()

		while (not self.isEmpty()):
			temp = self.peek()
			self.pop()
			self.__pushInPlace(buffer, temp)

		while (not buffer.isEmpty()):
			temp = buffer.peek()
			buffer.pop()
			self.push(temp)

	def __pushInPlace(self, buffer, value):

		valuePushed = False

		while (not valuePushed):
			if (buffer.isEmpty()):
				buffer.push(value)
				valuePushed = True
			elif (value < buffer.peek()):
				popped = buffer.peek()
				buffer.pop()
				self.push(popped)
			else:
				buffer.push(value)
				valuePushed = True

def main():
	stack = SortStack()
	stack.push(6)
	stack.push(3)
	stack.push(9)
	stack.push(10)
	stack.push(1)
	stack.push(8)
	stack.push(2)
	stack.push(7)

	stack.sort()

	while (not stack.isEmpty()):
		print stack.peek()
		stack.pop()
		
if __name__ == '__main__':
	main()