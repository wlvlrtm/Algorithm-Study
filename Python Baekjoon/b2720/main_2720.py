## 세탁소 사장 동혁
l = [25, 10, 5, 1]
t = int(input())
k = list()

for i in range(0, t) :
    c = int(input())

    for j in l :
        k.append(c // j)
        c = (c % j)

while (len(k) != 0) :
    for i in range(0, 4) :
        print(k[i], end=" ")

    k = k[4:]

    if (len(k) != 0) :
        print()