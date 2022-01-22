# -*- coding: utf-8 -*-

N, A, B = map(int, input().split(" "))
r = 0

for i in range(1, N+1):
    t = sum(list(map(int, list(str(i)))))
    if A <= t <= B:
        r += i
print(r)
