def move(n, source, destination, buffer):
	if (n == 1):
		if (destination and (destination[-1] < source[-1])):
			print 'Cant place disk'
			exit()

		destination.append(source.pop())
	else:
		move(n-1, source, buffer, destination)
		move(1, source, destination, buffer)
		move(n-1, buffer, destination, source)

def main():
	disks = int(raw_input('Enter number of disks: '))

	tower1 = []
	tower2 = []
	tower3 = []

	for i in xrange(disks, 0, -1):
		tower1.append(i)

	print 'Initial State: '
	print 'Tower 1: ', tower1
	print 'Tower 2: ', tower2
	print 'Tower 3: ', tower3

	move(len(tower1), tower1, tower3, tower2)

	print 'Final State: '
	print 'Tower 1: ', tower1
	print 'Tower 2: ', tower2
	print 'Tower 3: ', tower3

if __name__ == '__main__':
	main()
	