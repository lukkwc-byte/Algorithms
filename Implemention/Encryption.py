#!/bin/python3

import sys
import math

s = input().strip()
L = len(s)
y = math.floor(math.sqrt(L))
x = math.ceil(math.sqrt(L))
if x * y < L:
    y = x

o = []

for j in range(x):
    n = ""
    for i in range(y):
        if i * x + j <= len(s) - 1:
            n += s[i * x + j]
    o.append(n)
    
print(" ".join(o))
      


