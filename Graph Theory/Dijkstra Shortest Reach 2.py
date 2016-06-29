import heapq

class PriorityQ:
    def __init__(self):
        self.queue = []
        self.index = 0
    
    def isEmpty(self):
        return self.queue == []
    
    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1
    
    def pop(self):
        ret = heapq.heappop(self.queue)   
        return (ret[2], -ret[0])
    
    def __str__(self):
        return(str(self.queue))
    
    def update(self, existing_Item, new_Priority):
        for i, tupl in enumerate(self.queue):
            priority, index, item = tupl
            priority = -priority
            if item == existing_Item:
                self.queue.pop(i)
                self.push(existing_Item, new_Priority)
                break

def dijkstraBFS(N, edges, start):
    q = PriorityQ()
    maxDist= 400 * (N ** 2)
    
    d = [maxDist for i in range(N + 1)]
    d[start] = 0
    
    q.push(start, 0)
    
    for i in range(1, N + 1):
        if i != start:
            q.push(i, maxDist)
    
    while not q.isEmpty():
        current = q.pop()
        c, edgeD = current[0], current[1]
        
        neighbors = edges[c]
        for node, edgeD in neighbors.items():
            if d[c] + edgeD < d[node]:
                d[node] = d[c] + edgeD
                q.push(node, d[node])
   
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