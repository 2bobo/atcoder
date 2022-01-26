# -*- coding: utf-8 -*-

A, B = map(int, input().split(" "))

c = [" "] * 16
a_c = b_c = 0

for i in range(16):
    if i % 2 == 0 and b_c != B:
        c[i] = "B"
        b_c += 1
    elif i % 2 == 1 and a_c != A:
        c[i] = "A"
        a_c += 1
    #print(c)

if a_c == A and b_c == B:
    print("Yay!")
else:
    print(":(")

