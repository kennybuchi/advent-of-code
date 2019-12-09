inputFile = open('./2019/day6input.txt', 'r')
inputText = inputFile.read()

inputLines = inputText.splitlines()

#PART 1

def traverse(node, level):
    orbits = level
    if node in graph:
        for child in graph[node]:
            orbits += traverse(child, level + 1)
    return orbits

graph = {}

for line in inputLines:
    orbit = line.split(')')
    if orbit[0] in graph:
        graph[orbit[0]].append(orbit[1])
    else:
        graph[orbit[0]] = [orbit[1]]

orbitSum = traverse('COM', 0)
print('PART 1: ', orbitSum)

#PART 2

graph.clear()
for line in inputLines:
    orbit = line.split(')')
    if orbit[0] in graph:
        graph[orbit[0]].append(orbit[1])
    else:
        graph[orbit[0]] = [orbit[1]]
    if orbit[1] in graph:
        graph[orbit[1]].append(orbit[0])
    else:
        graph[orbit[1]] = [orbit[0]]

def shortestPath(start, end, graph, path = []):
    path = path + [start]
    if start == end:
        return path

    shortest = None
    for node in graph[start]:
        if node not in path:
            path2 = shortestPath(node, end, graph, path)
            if path2:
                if not shortest or len(path2) < len(shortest):
                    shortest = path2
    return shortest

path = shortestPath('YOU', 'SAN', graph)

print('PART 2: ', len(path) - 3)