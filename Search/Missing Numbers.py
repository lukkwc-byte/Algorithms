n = int(input())
A = [int(i) for i in input().split()]
m = int(input())
B = [int(i) for i in input().split()]

dA = {}
for num in A:
    if num in dA:
        dA[num] += 1
    else:
        dA[num] = 1

missing = []
for num in B:
    if num in dA:
        dA[num] -= 1
    else:
        missing.append(num)
        
for num, freq in dA.items():
    if freq < 0:
        missing.append(num)
missing = sorted(list(set(missing)))

print(" ".join([str(i) for i in missing]))