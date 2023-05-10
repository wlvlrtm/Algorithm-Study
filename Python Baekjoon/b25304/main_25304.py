## 영수증
x = int(input())    ## 총 금액
n = int(input())    ## 구매한 물건 종류의 수
y = 0

for i in (range(0, n)) :
    a, b = map(int, input().split())
    y += (a * b)

if (y == x) :
    print("Yes")
else :
    print("No")