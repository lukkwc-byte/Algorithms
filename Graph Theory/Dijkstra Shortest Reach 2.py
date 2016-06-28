def updateQ(queue, item):
    lis = []
    while not queue.empty():
        elem = queue.get()
        if elem[0] != item[0]:
            lis.append(elem)
    lis.append(item)
    for elem in lis:
        queue.put(elem)
    return queue

import queue as q
def dijkstraBFS(N, edges, start):
    queue = q.PriorityQueue()
    maxDist= 400 * (N ** 2)
    
    d = [maxDist for i in range(N + 1)]
    d[start] = 0
    
    if start > 1:
        for i in range(1, start):
            queue.put((i, maxDist))
    
    queue.put((start, 0))
    
    for i in range(start + 1, N + 1):
        queue.put((i, maxDist))
    
    while queue != []:
        current = queue.get()
        c, edgeD = current[0], current[1]
        
        neighbors = edges[c]
        for node, edgeD in neighbors.items():
            if d[c] + edgeD < d[node]:
                d[node] = d[c] + edgeD
                queue = updateQ(queue, (node, d[node]))
   
    for i, dist in enumerate(d):
        if dist == maxDist:
            d[i] = -1
    
    d.pop(start)
    d.pop(0)
    
    return d

def main():
    T = int(input())
    edges = {}
    
    for _ in range(T):
        N, M = [int(i) for i in input().split()]
        for i in range(N + 1):
            edges[i] = {}
        for i in range(M):
            node1, node2, edgeD = [int(i) for i in input().split()]
            if (node2 in edges[node1] and edgeD < edges[node1][node2]) or node2 not in edges[node1]:
                    edges[node1][node2] = edgeD
                    edges[node2][node1] = edgeD
        start = int(input())
        d = dijkstraBFS(N, edges, start)
        print(" ".join([str(i) for i in d]))
main()
