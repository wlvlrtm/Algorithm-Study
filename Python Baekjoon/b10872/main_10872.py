## 팩토리얼
n = int(input())
r = n

if (n == 0) :
    r = 1
else :
    for i in range(1, n) :
        r *= i

print(r)