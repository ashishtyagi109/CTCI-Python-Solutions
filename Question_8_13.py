from numpy import zeros

class Box(object):

	def __init__(self, width, length, height):
		self.width = width
		self.length = length
		self.height = height
	
	def __repr__(self):
		return str(self.height)

	def canBeAbove(self, other):
		return (self.width > other.width) and \
			   (self.length > other.length) and \
			   (self.height > other.height)


def maxHeight(boxes):
	boxMap = zeros((len(boxes)))
	boxes.sort(key = lambda box: box.height, reverse = True)
	maxHeight = 0

	for i in xrange(len(boxes)):
		height = createStack(i, boxes, boxMap)
		maxHeight = max(maxHeight, height)

	return maxHeight

def createStack(bottomIndex, boxes, boxMap):
	if (bottomIndex < len(boxes) and boxMap[bottomIndex] != 0):
		return boxMap[bottomIndex]

	maxHeight = 0
	bottom = boxes[bottomIndex]

	for i in xrange(bottomIndex + 1, len(boxes)):
		if (bottom.canBeAbove(boxes[i])):
			height = createStack(i, boxes, boxMap)
			maxHeight = max(maxHeight, height)

	maxHeight += bottom.height
	boxMap[bottomIndex] = maxHeight
	return maxHeight
