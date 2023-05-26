## 소수
m = int(input())
n = int(input())
l = list()

for i in range(m, n+1) :
    t = True

    if (i > 1) :
        for j in range(2, i) :
            if (i % j == 0) :
                t = False
                break

        if (t == True) :
            l.append(i)

if (len(l) > 0) :
    print(sum(l))
    print(min(l))
else:
    print(-1)