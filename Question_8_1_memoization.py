from numpy import full

def tripSteps(n, memo = None):
	if (memo is None):
		memo = full((n+1), -1)
		return tripSteps(n, memo)

	if (n < 0):
		return 0
	if (n == 0):
		return 1
	if (memo[n] > -1):
		return memo[n]

	memo[n] = tripSteps(n-1, memo) + tripSteps(n-2, memo) + tripSteps(n-3, memo)
	return memo[n]

def main():
	n = int(raw_input('Enter number of steps: '))
	answer = tripSteps(n)
	print 'There are {} number of ways to reach {} steps'.format(answer, n)

if __name__ == '__main__':
	main()