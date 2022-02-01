# -*- coding: utf-8 -*-
import math

N = int(input())
l = int(math.sqrt(N))
ans = 10 ** 13

for i in range(1, l+1):
    #print(i)
    #print(ans)
    if (N % i) == 0:
        if ans > abs(i + (N // i) - 2):
            ans = abs(i + (N // i) - 2)
print(ans)

