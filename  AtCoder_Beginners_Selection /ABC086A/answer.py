# -*- coding: utf-8 -*-

a, b = map(int, input().split(" "))

c = (a*b) % 2

if c == 0:
    print("Even")
else:
    print("Odd")
