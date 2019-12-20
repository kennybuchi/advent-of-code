import networkx as nx
import matplotlib.pyplot as plt

inputFile = open('./2019/day18input.txt', 'r')
inputText = inputFile.read()
maze = inputText.splitlines()

width = len(maze[0])
length = len(maze)

graph = nx.Graph()

directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

keys = {}
doors = {}

for i in range(1, length - 1):
    for j in range(1, width - 1):
        if maze[i][j] != '#':
            graph.add_node((i, j))
            #get key/door/start location
            if maze[i][j] == '@':
                keys[maze[i][j]] = (i, j)
            elif maze[i][j].islower():
                keys[maze[i][j]] = (i, j)
                doors[(i, j)] = maze[i][j].lower()
            elif maze[i][j].isupper():
                doors[(i, j)] = maze[i][j].lower()

            #make edges:
            for d in directions:
                i2, j2 = i + d[0], j + d[1]
                if maze[i2][j2] != '#':
                    graph.add_edge((i, j), (i2, j2))

start = keys['@']

distances = {}
blockers = {}

for key in keys.keys():
    distances[key] = {}
    blockers[key] = set('@')

for key in keys.keys():
    for key2 in keys.keys():
        if key == key2:
            continue
        path = nx.bidirectional_shortest_path(graph, keys[key], keys[key2])
        if key == '@':
            for i in range(len(path) - 1):
                pair = path[i]
                if pair in doors:
                    blockers[key2].add(doors[pair])
        distances[key][key2] = len(path) - 1
        distances[key2][key] = len(path) - 1

# for key in keys.keys():
#     if key == '@':
#         continue
#     blockers['@'][key].add('@')

def getTotalDistance(arr, distances):
    dist = 0
    for i in range(len(arr) - 1):
        dist += distances[arr[i]][arr[i+1]]

    return dist

visited = set()
toVisit = set()
toVisitNew = set()

toVisit.add('@')



dependencies = nx.DiGraph()

for key in keys:
    dependencies.add_node(key)

while len(visited) < len(keys):
    toVisitNew.clear()
    for v in toVisit:
        visited.add(v)
    for item in toVisit:
        for key in keys:
            if key == item or key in visited:
                continue

            if key not in toVisitNew and blockers[key].issubset(set(toVisit)):
                for it in blockers[key]:
                    dependencies.add_edge(it, key)
                toVisitNew.add(key)

    for key in keys:
        for v in toVisit:
            if v in blockers[key]:
                blockers[key].remove(v)

    toVisit = toVisitNew.copy()

# rework this, too slow

topological = list(nx.all_topological_sorts(dependencies))

shortest = []
shortestSteps = 999999

totalPaths = len(topological)
for p in topological:
    steps = getTotalDistance(p, distances)
    if steps < shortestSteps:
        shortest = p
        shortestSteps = steps


print(shortest)
print(shortestSteps)
