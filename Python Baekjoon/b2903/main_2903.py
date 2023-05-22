## 중앙 이동 알고리즘
n = int(input())
x = 2
a = 1

for i in range(0, n) :
    x += a
    a *= 2

print(x**2)