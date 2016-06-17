t = int(input())

def moveH(ci, cj, f, m):
    j = cj
    neighbours = []
    while j < m and f[ci][j] != "X":
        neighbours.append((ci, j))
        j += 1
    
    j = cj
    while j > 0 and f[ci][j] != "X":
        neighbours.append((ci, j))
        j -= 1
    
    return neighbours

def moveV(ci, cj, f, n):
    i = ci
    neighbours = []
    while i < n and f[i][cj] != "X":
        neighbours.append((i, cj))
        i += 1
    
    i = ci
    while i > 0 and f[i][cj] != "X":
        neighbours.append((i, cj))
        i -= 1
    
    return neighbours

def get_Neighbours(c, f, n, m):
    neighbours = []
    ci, cj = c[0], c[1]
    neighbours += moveH(ci, cj, f, m)
    neighbours += moveV(ci, cj, f, n)
    return neighbours
            
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    f = []
    v = []
    d = []
    
    for i in range(n):
        v.append([0 for x in range(m)])
    
    for i in range(n):
        d.append([0 for x in range(m)])
    
    for i in range(n):
        row = list(input())
        for j, pos in enumerate(row):
            if pos == "M":
                b = (i, j)
        f.append(row)
   
    k = int(input())
    s = []
    s.append(b)
    found = False
    v[b[0]][b[1]] = 1
    h = 0
    while(s != [] and found == False):
        c = s.pop()
        neighbours = get_Neighbours(c, f, n, m)
        print(c, neighbours)
        for neighbour in neighbours:
            if f[neighbour[0]][neighbour[1]] == "*":
                found = True
                h = d[c[0]][c[1]] + 1
                break
            elif v[neighbour[0]][neighbour[1]] == 0:
                v[neighbour[0]][neighbour[1]] = 1
                d[neighbour[0]][neighbour[1]] = d[c[0]][c[1]] + 1 
                s.append(neighbour)
            else:
                d[neighbour[0]][neighbour[1]] = d[c[0]][c[1]] + 1 if (d[c[0]][c[1]] + 1 < d[neighbour[0]][neighbour[1]]) else d[neighbour[0]][neighbour[1]]
    print(d)
    if h == k:
        print("Impressed")
    else:
        print("Oops!")
            
        