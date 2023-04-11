import math
maxsize = float('inf')

with open('salesman.txt', 'r') as f:
    graph = []
    for line in f:
        row = [int(num) for num in line.split()]
        graph.append(row)

l = len(graph)

def dijktra(graph, source, dest):
    shortest = [0 for i in range(len(graph))]
    selected = [source]
    l = len(graph)
    # Base case from source
    inf = 10000000
    min_sel = inf
    for i in range(l):
        if (i == source):
            shortest[source] = 0  # graph[source][source]
        else:
            if (graph[source][i] == 0):
                shortest[i] = inf
            else:
                shortest[i] = graph[source][i]
                if (shortest[i] < min_sel):
                    min_sel = shortest[i]
                    ind = i

    if (source == dest):
        return 0
    # Dijktra's in Play
    selected.append(ind)
    while (ind != dest):
        # print('ind',ind)
        for i in range(l):
            if i not in selected:
                if (graph[ind][i] != 0):
                    # Check if distance needs to be updated
                    if ((graph[ind][i] + min_sel) < shortest[i]):
                        shortest[i] = graph[ind][i] + min_sel
        temp_min = 1000000
        # print('shortest:',shortest)
        # print('selected:',selected)

        for j in range(l):
            if j not in selected:
                if (shortest[j] < temp_min):
                    temp_min = shortest[j]
                    ind = j
        min_sel = temp_min
        selected.append(ind)

    return shortest[dest]

with open("salesmandists.txt", "w") as file2:
    for x in range(l):
        for y in range(l):
            print(dijktra(graph, x, y), end=' ')
            file2.write(str(dijktra(graph, x, y))  + " ")
            if (y == l - 1):
                print('\n')
                file2.write('\n')

def copyToFinal(curr_path):
    final_path[:N + 1] = curr_path[:]
    final_path[N] = curr_path[0]

def firstMin(adj, i):
    min = maxsize
    for k in range(N):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min

def secondMin(adj, i):
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif (adj[i][j] <= second and
              adj[i][j] != first):
            second = adj[i][j]

    return second

def TSPRec(adj, curr_bound, curr_weight,
           level, curr_path, visited):
    global final_res

    if level == N:

        if adj[curr_path[level - 1]][curr_path[0]] != 0:

            curr_res = curr_weight + adj[curr_path[level - 1]] \
                [curr_path[0]]
            if curr_res < final_res:
                copyToFinal(curr_path)
                final_res = curr_res
        return

    for i in range(N):
        if (adj[curr_path[level - 1]][i] != 0 and
                visited[i] == False):
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]
            if level == 1:
                curr_bound -= ((firstMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                curr_bound -= ((secondMin(adj, curr_path[level - 1]) +
                                firstMin(adj, i)) / 2)
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                TSPRec(adj, curr_bound, curr_weight,
                       level + 1, curr_path, visited)
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp

            visited = [False] * len(visited)
            for j in range(level):
                if curr_path[j] != -1:
                    visited[curr_path[j]] = True

def TSP(adj):
    curr_bound = 0
    curr_path = [-1] * (N + 1)
    visited = [False] * N

    for i in range(N):
        curr_bound += (firstMin(adj, i) +
                       secondMin(adj, i))

    curr_bound = math.ceil(curr_bound / 2)
    visited[0] = True
    curr_path[0] = 0
    TSPRec(adj, curr_bound, 0, 1, curr_path, visited)

with open('salesmandists.txt', 'r') as file3:
    graphdist = []
    for line in file3:
        row = [int(num) for num in line.split()]
        graphdist.append(row)

N = len(graphdist)

final_path = [None] * (N + 1)
visited = [False] * N
final_res = maxsize

TSP(graph)

print("Minimum cost :", final_res)
print("Path Taken : ", end=' ')
for i in range(N + 1):
    print(final_path[i], end=' ')
