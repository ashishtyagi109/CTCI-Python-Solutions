def buildOrder(listOfProjects, listOfDependencies):
	adjList = {}
	InDeg = {}
	for project in listOfProjects:
		adjList[project] = []
		InDeg[project] = 0

	for first, second in listOfDependencies:
		adjList[second].append(first)
		InDeg[first] += 1

	nodesWithoutInEdges = []

	for project in InDeg:
		if InDeg[project] == 0:
			nodesWithoutInEdges.append(project)

	buildOrder = []

	while nodesWithoutInEdges: # List not empty
		node = nodesWithoutInEdges.pop()
		for dependent in adjList[node]:
			InDeg[dependent] -= 1
			if InDeg[dependent] == 0:
				nodesWithoutInEdges.append(dependent)
		buildOrder.append(node)

	if len(buildOrder) == len(listOfProjects):
		return buildOrder
	else:
		return None

if __name__ == '__main__':
	projects = ['a','b','c','d','e','f']
	dependencies1 = [('d','a'), ('b','f'), ('d','b'), ('a','f'), ('c','d')]
	dependencies2 = [('d','a'), ('b','f'), ('d','b'), ('a','f'), ('c','d'), ('f', 'e'), ('e','b')] # No solution exists
	order1 = buildOrder(projects, dependencies1)
	order2 = buildOrder(projects, dependencies2)

	if order1 is not None:
		print order1
	else:
		print 'Error'
	if order2 is not None:
		print order2
	else:
		print 'Error'
