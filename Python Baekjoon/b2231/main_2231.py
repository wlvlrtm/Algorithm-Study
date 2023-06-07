## 분해합
n = int(input())

for i in range(1, n+1) :
    s = sum((map(int, str(i))))
    m = i + s

    if (m == n) :
        print(i)
        break
    if (i == n) :
        print(0)