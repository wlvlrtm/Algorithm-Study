## 색종이
n = int(input())
l = list()

for i in range(0, 100) :
    l.append([0] * 100)

for j in range(0, n) :
    x, y = map(int, input().split())

    for k in range(y, y+10) :
        for p in range(x, x+10) :
            l[k][p] = 1

r = 0

for o in range(0, 100) :
    r += l[o].count(1)

print(r)