# -*- coding: utf-8 -*-

def waru(waru_n):
    return int(waru_n / 2)


def check(check_bl):
    for check_n in check_bl:
        if check_n % 2 != 0:
            return 1

_ = int(input())
b = list(map(int, input().split(" ")))

r = 0
f = 0

while f == 0:
    if check(b) == 1:
        print(r)
        exit()
    else:
        b = list(map(waru, b))
        r += 1
