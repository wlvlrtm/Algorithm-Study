## 세로 읽기
l = list()
m = 0
k = 0

for i in range(0, 5) :
    t = list(input())
    l.append(t)

    if (len(t) > m) :
        m = len(t)

for i in range(0, m) :
    for j in range(0, len(l)) :
        if (k >= len(l[j])) :
            continue

        print(l[j][k], end="")
    k += 1