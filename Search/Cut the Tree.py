import sys
sys.setrecursionlimit(1000000)


def DFS_Subtree(c, edges):
    global t_values, v_values, min_diff, total
    neighbours = edges[c]
    t_values[c] = v_values[c - 1]
    if not (len(neighbours) == True and t_values[neighbours[0]] == True):
        for neighbour in neighbours:
            if t_values[neighbour] == 0:
                t_values[c] += DFS_Subtree(neighbour, edges)
    diff = abs(t_values[c] - (total - t_values[c]))
    min_diff = diff if diff < min_diff else min_diff
    return t_values[c]

n = int(input())
v_values = [int(i) for i in input().split()]
t_values = [0] * (n + 1)
total = sum(v_values)
min_diff = total
edges = {}

for i in range(n - 1):
    v1, v2 = [int(x) for x in input().split()]
    if v1 in edges:
        edges[v1].append(v2)
    else:
        edges[v1] = [v2]
    if v2 in edges:
        edges[v2].append(v1)
    else:
        edges[v2] = [v1]

DFS_Subtree(1, edges)

print(min_diff)


         
    
    

    