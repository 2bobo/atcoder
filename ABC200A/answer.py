# -*- coding: utf-8 -*-

N = int(input())

r = int(N / 100)
if (N % 100) != 0:
    r = r + 1

print(r)
