import numpy

def getRobotPath(grid):
	if (grid is None):
		return None
	cache = {}
	path = []
	rows, cols = grid.shape
	if (pathHelper(rows-1, cols-1, grid, cache, path)):
		return path
	return None

def pathHelper(row, col, grid, cache, path):
	# Out of bounds
	if (row < 0 or col < 0):
		return False
	# Block in grid is off limits
	if (not grid[row, col]):
		return False
	if (row,col) in cache:
		return cache[(row,col)]

	isAtOrigin = (row == 0) and (col == 0)
	success = False

	if (isAtOrigin or pathHelper(row-1, col, grid, cache, path) or \
					pathHelper(row, col-1, grid, cache, path)):
		path.append((row,col))
		success = True

	cache[(row,col)] = success
	return success

def main():
	rows = int(raw_input('Enter number of rows: '))
	cols = int(raw_input('Enter number of cols: '))

	grid = numpy.random.randint(0, 2, (rows, cols))
	grid = grid.astype(bool, copy=False)

	grid[0][0] = True # Origin is accessible
	grid[rows-1][cols-1] = True # Destination is accessible

	print 'Grid: '
	print grid

	answer = getRobotPath(grid)

	if answer is None:
		print 'No path exists'
	else:
		print 'path is: ', answer

if __name__ == '__main__':
	main()