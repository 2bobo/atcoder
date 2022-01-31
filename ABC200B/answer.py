# -*- coding: utf-8 -*-

n, K = map(int, input().split(" "))

for i in range(K):
    #print(n)
    if (n % 200) == 0:
        n = n // 200
    else:
        n = int(str(n)+"200")

print(n)
