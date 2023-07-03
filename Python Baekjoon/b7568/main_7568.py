## 덩치
n = int(input())
l = list()

for _ in range(n) :
    a, b = map(int, input().split())
    l.append((a, b))

for i in range(n) :
    c = 1

    for j in range(n) :
        if (l[i][0] < l[j][0] and l[i][1] < l[j][1]) :
            c += 1

    print(c, end=' ')