def BFS(N, edges, S):
    s = [S]
    visited = set()
    visited.add(S)
    d = [0 for i in range(N + 1)]
    while s != []:
        c = s.pop(0)
        nx = edges[c]
        for n in nx:
            if n not in visited:
                d[n] = d[c] + 6
                s.append(n)
                visited.add(n)
    for i, dx in enumerate(d):
        if dx == 0:
            d[i] = -1
    d.pop(S)
    return d

T = int(input())
for _ in range(T):
    N, M = [int(i) for i in input().split()]
    edges = {}
    for i in range(N + 1):
        edges[i] = []
    for i in range(M):
        n1, n2 = [int(i) for i in input().split()]
        edges[n1].append(n2)
        edges[n2].append(n1)
    S = int(input())
    d = BFS(N, edges, S)
    print(" ".join([str(i) for i in d[1:]]))
