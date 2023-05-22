## 분수 찾기
x = int(input())
l = 1
a, b = 0, 0

## 짝수: 분자 +1, 분모 -1
## 홀수: 분자 -1, 분모 +1

while x > l :
    x -= l
    l += 1

if l % 2 == 0:  ## 짝수
    a = x
    b = l - x +1
else :          ## 홀수
    a = l - x + 1
    b = x

print(a,"/",b, sep="")