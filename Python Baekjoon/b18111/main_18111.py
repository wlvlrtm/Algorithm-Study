## 마인크래프트
import sys

n, m, b = map(int, sys.stdin.readline().split())
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
resTime = 64000000

for i in range(257) :
    inInv = 0
    outInv = 0

    for j in range(n) :
        for k in range(m) :
            if (world[j][k] < i) :
                outInv += (i - world[j][k])
            else :
                inInv += (world[j][k] - i)

    inv = b + inInv

    if (inv >= outInv) :
        time = (2 * inInv) + outInv

        if (time <= resTime) :
            resTime = time
            height = i

print(resTime, height)