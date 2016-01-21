import numpy

GRID_SIZE = 8

def placeQueens(row, columns):
	if (row == GRID_SIZE): # Valid placement found
		print columns
	else:
		for pos in xrange(GRID_SIZE):
			if(isValid(row, pos, columns)):
				columns[row] = pos # Place queen
				placeQueens(row + 1, columns)
				#columns[row] = -1 # Remove queen for next iteration

def isValid(row1, col1, columns):
	# Only need to check if placement is in same column/diagonal as a previous placement
	
	for row2 in xrange(row1):
		col2 = columns[row2]

		# Check if columns are same
		if (col1 == col2):
			return False

		# For 2 queens to be on same diagonal, absolute difference of their row and column placement \
		# should be the same

		colDifference = abs(col1 - col2)
		rowDifference = row1 - row2
		if (colDifference == rowDifference):
			return False

	return True

def main():
	columns = numpy.full((8), -1)
	print columns
	placeQueens(0, columns)

if __name__ == '__main__':
	main()

