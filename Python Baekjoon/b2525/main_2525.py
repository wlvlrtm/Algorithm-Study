## 오븐 시계
a, b = map(int, input().split())
c = int(input())

## a, (b + c)
b += c

## b 정리
while (b > 59) :
    b -= 60
    a += 1

    if (a == 24) :
        a = 0

print(a, b)