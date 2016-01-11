# Another benefit of this solution over the memoized solution \
# (other than the obvious O(1) memory) \
# is that python seamlessly changes from int to long, which has infinite precision

def tripSteps(n):
	if (n < 3):
		return n
	first = 1
	second = 1
	third = 2

	for i in xrange(3, n):
		temp = first + second + third
		first = second
		second = third
		third = temp

	return first + second + third

def main():
	n = int(raw_input('Enter number of steps: '))
	answer = tripSteps(n)
	print 'There are {} number of ways to reach {} steps'.format(answer, n)

if __name__ == '__main__':
	main()