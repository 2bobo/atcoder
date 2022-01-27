# -*- coding: utf-8 -*-

N, M = map(int, input().split(" "))

c = {
    "+++": [],
    "++-": [],
    "+-+": [],
    "-++": [],
    "--+": [],
    "-+-": [],
    "+--": [],
    "---": []
}
cr = {}

for i in range(N):
    x, y, z = map(int, input().split(" "))
    c["+++"].append(x + y + z)
    c["++-"].append(x + y - z)
    c["+-+"].append(x - y + z)
    c["-++"].append(-x + y + z)
    c["--+"].append(-x - y + z)
    c["-+-"].append(-x + y - z)
    c["+--"].append(x - y - z)
    c["---"].append(-x - y - z)

    c["+++"].sort(reverse=True)
    c["++-"].sort(reverse=True)
    c["+-+"].sort(reverse=True)
    c["-++"].sort(reverse=True)
    c["--+"].sort(reverse=True)
    c["-+-"].sort(reverse=True)
    c["+--"].sort(reverse=True)
    c["---"].sort(reverse=True)

    cr["+++"] = sum(c["+++"][0:M])
    cr["++-"] = sum(c["++-"][0:M])
    cr["+-+"] = sum(c["+-+"][0:M])
    cr["-++"] = sum(c["-++"][0:M])
    cr["--+"] = sum(c["--+"][0:M])
    cr["-+-"] = sum(c["-+-"][0:M])
    cr["+--"] = sum(c["+--"][0:M])
    cr["---"] = sum(c["---"][0:M])

    #print(c)

print(max(cr["+++"], cr["++-"], cr["+-+"], cr["-++"], cr["--+"], cr["-+-"], cr["+--"], cr["---"]))
    
