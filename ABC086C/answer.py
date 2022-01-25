# -*- coding: utf-8 -*-


N = int(input())

t = 0
c = 0
x = 0
y = 0

for i in range(N):
    s_t, s_x, s_y = map(int, input().split(" "))
    #print("----")
    #print(s_t, s_x, s_y)
    #print("----")
    for c in range(t+1, s_t+1):
        #print(c)
        if x < s_x:
            x += 1
            #print("x+")
        elif x > s_x:
            x -= 1
            #print("x-")
        elif y < s_y:
            y += 1
            #print("y+")
        elif y > s_y:
            y -= 1
            #print("y-")
        elif t_x == x and t_y == y:
            x += 1
            #print("e")

        #print(c, x, y)

        if c == s_t and (x != s_x or y != s_y):
            print("No")
            exit()
        t_x = x
        t_y = y
    t = c
print("Yes")
