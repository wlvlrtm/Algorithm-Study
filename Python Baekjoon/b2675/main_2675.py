## 문자열 반복
i = ""
l = list()

s = int(input())

for a in range(0, s) :
    r, p = map(str, input().split())
    r = int(r)

    for b in p :
        i += (b * r)

    l.append(i)
    i = ""

for c in l :
    print(c)