# As strings are immutable in python, we need a fast way to append to our new string.
# Using https://waymoot.org/home/python_string/ as reference, the following is the fastest way that works for our problem
from cStringIO import StringIO
def URLify(str):
	answer = StringIO()
	spaceFlag = False

	for c in str:
		if c == ' ':
			if not spaceFlag:
				spaceFlag = True
		else:
			if spaceFlag:
				answer.write('%20')
				answer.write(c)
				spaceFlag = False
			else:
				answer.write(c)

	# Edge case of space(s) at the end
	if spaceFlag:
		answer.write('%20')

	return answer.getvalue()

input = raw_input('Enter String: ')
print URLify(input)