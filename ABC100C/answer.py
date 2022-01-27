# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split(" ")))
r = 0

for i in range(N):
    t = 0
    if A[i] % 2 == 0:
        tmp = A[i]
        while tmp % 2 == 0:
            tmp = tmp / 2
            r += 1

print(r)
