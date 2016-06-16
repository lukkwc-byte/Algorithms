def flood(i, j, n, m):
    if g[i][j] == 0:
        return 0
    count = 1
    g[i][j] = 0
    if i + 1 < m:
        count += flood(i + 1, j, n, m)
        if j + 1 < n:
            count += flood(i + 1, j + 1, n, m)
        if j - 1 >= 0:
            count += flood(i + 1, j - 1, n, m)
    if i - 1 > 0:
        count += flood(i - 1, j, n, m)
        if j + 1 < n:
            count += flood(i - 1, j + 1, n, m)
        if j - 1 >= 0:
            count += flood(i - 1, j - 1, n, m)
    if j + 1 < n:
        count += flood(i, j + 1, n, m)
    if j - 1 >= 0:
        count += flood(i, j - 1, n, m)     
    return count

m = int(input())
n = int(input())
g = []
for i in range(m):
    g.append([int(char) for char in input().split()])

largest = 0
for i in range(m):
    for j in range(n):
        current = flood(i, j, n, m)
        if current > largest:
            largest = current

print(largest)
