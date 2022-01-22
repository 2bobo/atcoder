# -*- coding: utf-8 -*-


coins = {"500": int(input()), "100": int(input()), "50": int(input())}
result = int(input())
cnt = 0

#print(f"500: {coins['500']} 100: {coins['100']} 50: {coins['50']}")
#print(result)


for a in range(coins["500"]+1):
    #print(f"a:{a}")
    for b in range(coins["100"]+1):
        #print(f"b:{b}")
        for c in range(coins["50"]+1):
            #print(f"{a}+{b}+{c}={(a*500)+(b*100)+(c*50)}")
            if ((a*500)+(b*100)+(c*50)) == result:
                cnt += 1
                #print(result)
print(cnt)

