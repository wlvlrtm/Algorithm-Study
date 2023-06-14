## 팩토리얼 0의 개수
n = int(input())
r = n
c = 0

if (n == 0) :
    print(0)
else :
    for i in range(1, n) :
        r *= i

    r = str(r)

    for j in range(len(r)-1, -1, -1) :
        if (r[j] == "0") :
            c += 1
        else :
            break

    print(c)