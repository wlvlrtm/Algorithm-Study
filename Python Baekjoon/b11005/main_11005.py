## 진법 변환 2
n, b = map(int, input().split())
num = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = str()

while (n != 0) :
    r += num[n % b]
    n = (n // b)

print(r[::-1])