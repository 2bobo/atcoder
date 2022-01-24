# -*- coding: utf-8 -*-

S = input()
T = ["dreamer", "eraser", "dream", "erase"]

m = S[::-1]
r = ""
k = ""
l = []
for a in T:
    l.append(a[::-1])

while 1:
    if m == r:
        print("YES")
        exit()
    elif m.startswith(r+l[0]):
        k = l[0]
    elif m.startswith(r+l[1]):
        k = l[1]
    elif m.startswith(r+l[2]):
        k = l[2]
    elif m.startswith(r+l[3]):
        k = l[3]
    else:
        print("NO")
        exit()
    r = r + k
