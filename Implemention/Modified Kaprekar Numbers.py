p, q = int(input()), int(input())
l = []
for i in range(p, q + 1):
    square = str(i ** 2)
    d = len(str(i))
    right = int(square[len(square) - d : len(square)])
    if len(square) % 2 == 0:
        left = int(square[:d])
    elif len(square) % 2 != 0 and len(square) > 1:
        left = int(square[:d - 1])
    else:
        left = 0
    if left + right == i:
        l.append(str(i))
if len(l) == 0:
    print("INVALID RANGE")
else:
    print(" ".join(l))