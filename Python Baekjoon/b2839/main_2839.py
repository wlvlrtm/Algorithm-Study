## 설탕 배달
n = int(input())
r = 0

while (n >= 0) :
    if (n % 5 == 0) :
        r += (n // 5)
        break

    n -= 3
    r += 1

if (n >= 0) :
    print(r)
else :
    print(-1)