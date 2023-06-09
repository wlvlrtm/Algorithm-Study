## 직각 삼각형
r = list()

while (True) :
    l = list(map(int, input().split()))
    l.sort()

    if (l[0] + l[1] + l[2] == 0) :
        break
    elif ((l[2] ** 2) == (l[0] ** 2) + (l[1] ** 2)) :
        r.append("right")
    else :
        r.append("wrong")

for i in r :
    print(i)