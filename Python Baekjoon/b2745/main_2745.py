## 진법 변환
n, b = map(str, input().split())
n = n[::-1]
b = int(b)
x = len(n)

num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = 0

for i in range(0, x) :
    r += (num.index(n[i]) * (b**i))

print(r)