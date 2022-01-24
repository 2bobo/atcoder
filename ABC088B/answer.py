# -*- coding: utf-8 -*-

N = int(input())
C = list(map(int, input().split(" ")))
C.sort(reverse=True)

a = C[0::2]
b = C[1::2]

#print(a)
#print(b)

#print(C)
#print("---")

print(sum(a)-sum(b))
