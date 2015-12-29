# Assume graph given in adjacency list format, nodes given as int indexes
from numpy import zeros
from Queue import *

def routeChecker(graph,s, t):
	if s == t:
		return True

	queue = Queue()
	visited = zeros((len(graph)), dtype = bool)
	visited[s] = True
	queue.put(s)

	while not queue.empty():
		node = queue.get()
		for temp in graph[node]:
			if not visited[temp]:
				if temp == t:
					return True
				visited[temp] = True
				queue.put(temp)
	return False