## 분수 찾기
x = int(input())
l = 1
a, b = 0, 0

while (x > l) :
    x -= l
    l += 1

if (l % 2 == 0) :
    a = x
    b = l - x + 1
else :
    a = l - x + 1
    b = x

print(a, "/", b, sep="")