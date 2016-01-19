from numpy import zeros

def coinWays(n):
	if (n < 1):
		return 0

	denom = [25, 10, 5, 1]
	memo = zeros((n, 3))
	return coinCount(n, memo, denom, 0)

def coinCount(n, memo, denom, index):
	if (index == len(denom) - 1): # Last denom
		return 1
	if (n == 0):
		return 1
	if (memo[n-1][index] != 0):
		return memo[n-1][index]

	ways = 0
	i = 0

	while (i <= n/denom[index]):
		nRemaining = n - (i*denom[index])
		ways += coinCount(nRemaining, memo, denom, index + 1)
		i += 1

	memo[n-1][index] = ways
	return ways

def main():
	input = int(raw_input('Enter number of cents: '))
	answer = coinWays(input)
	print 'There are {} ways to get {} cents'.format(answer, input)

if __name__ == '__main__':
	main()
