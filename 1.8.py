def zeroCheck(matrix):
	rows = set()
	cols = set()
	row, col = matrix.shape

	for i in xrange(row):
		for j in xrange(col):
			if matrix[i][j] == 0:
				rows.add(i)
				cols.add(j)

	for r in rows:
		for index in xrange(col):
			matrix[r][index] = 0
	for c in cols:
		for index in xrange(row):
			matrix[index][c] = 0

	return matrix

import numpy as np
matrix = np.empty([3,3])
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3
matrix[1][0] = 4
matrix[1][1] = 0
matrix[1][2] = 5
matrix[2][0] = 6
matrix[2][1] = 7
matrix[2][2] = 0

# Only (0,0) should be nonzero
print 'input: '
print matrix
print 'output: '
print zeroCheck(matrix)