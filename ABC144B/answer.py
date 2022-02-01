# -*- coding: utf-8 -*-

N = int(input())

l = []

for a in range(1, 10):
    for b in range(1, 10):
        l.append(a*b)

#print(l)
if N in l:
    print("Yes")
else:
    print("No")