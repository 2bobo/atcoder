# -*- coding: utf-8 -*-

N = int(input())
A = list(map(int, input().split(" ")))

r = [x % 200 for x in A]
cnt = [0] * 200

c = 0
for x in r:
#    print(cnt[x])
    c += cnt[x]
    cnt[x] += 1

print(c)
