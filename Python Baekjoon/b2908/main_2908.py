## 상수
a, b = map(str, input().split())

la = a[::-1]
lb = b[::-1]

la = int(la)
lb = int(lb)

if (la > lb) :
    print(la)
else :
    print(lb)