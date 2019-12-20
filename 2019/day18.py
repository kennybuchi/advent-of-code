import networkx as nx

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
            if maze[i][j].islower() or maze[i][j] == '@':
                keys[maze[i][j]] = (i, j)
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
    blockers[key] = {}
    for key2 in keys.keys():
        if key == key2:
            continue
        blockers[key][key2] = set()

for key in keys.keys():
    for key2 in keys.keys():
        if key == key2:
            continue
        path = nx.bidirectional_shortest_path(graph, keys[key], keys[key2])
        for pair in path:
            if pair in doors or pair in keys:
                blockers[key][key2].add(doors[pair])
                blockers[key2][key].add(doors[pair])
        distances[key][key2] = len(path) - 1
        distances[key2][key] = len(path) - 1

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
    for item in toVisit:
        for v in toVisit:
            visited.add(v)
        for key in keys:
            if key == item or key in visited:
                continue

            for v in visited:
                if v in blockers[item][key]:
                    blockers[item][key].remove(v)

            if len(blockers[item][key]) == 0:
                dependencies.add_edge(item, key)
                toVisitNew.add(key)

    toVisit = toVisitNew.copy()


abc = list(nx.topological_sort(dependencies))
print(getTotalDistance(abc, distances))