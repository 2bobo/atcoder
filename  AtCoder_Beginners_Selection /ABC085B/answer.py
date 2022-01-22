# -*- coding: utf-8 -*-

N = int(input())

m = []
for i in range(N):
    m.append(int(input()))

m = list(set(m))

print(len(m))