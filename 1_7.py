import numpy as np

def rotate(matrix, n):
	for layer in xrange(n/2):
		first = layer
		last = n - 1 - layer
		while first < last:
			# Save Top
			temp = matrix[layer,first]

			# Left to Top
			matrix[layer,first] = matrix[n-1-first, layer]

			# Bottom to Left
			matrix[n-1-first, layer] = matrix[n-1-layer, n-1-first]

			# Right to Bottom
			matrix[n-1-layer, n-1-first] = matrix[first, n-1-layer]

			# Top to Right
			matrix[first, n-1-layer] = temp

			first +=1

	return matrix

N = 4
matrix = np.random.rand(N, N)

print 'Random image: '
print matrix
print 'Rotated image: '
print rotate(matrix, N)