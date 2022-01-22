# -*- coding: utf-8 -*-

N, Y = map(int, input().split(" "))
r = None

a = b = c = 0

if N * 10000 == Y:
    print(f"{N} 0 0")
    exit()
elif N * 5000 == Y:
    print(f"0 {N} 0")
    exit()
elif N * 1000 == Y:
    print(f"0 0 {N}")
    exit()
else:
    for a in range(N+1):
        if (a * 10000)+((N - a) * 5000) >= Y:
            for b in range((N-a)+1):
                c = N-(a+b)
                if N == a+b+c:
                    if Y == (a*10000)+(b*5000)+(c*1000):
                        r = f"{ a } { b } { c }"
                        print(r)
                        exit()
    if r is None:
        print("-1 -1 -1")
