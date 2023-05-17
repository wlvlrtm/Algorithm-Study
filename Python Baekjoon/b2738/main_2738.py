## 행렬 덧셈
n, m = map(int, input().split())
a = list()
b = list()

for i in range(0, n) :
    r = list(map(int, input().split()))
    a.append(r)

for j in range(0, n) :
    r = list(map(int, input().split()))
    b.append(r)

for k in range(0, n) :
    for l in range(0, m) :
        print(a[k][l] + b[k][l], end=" ")

    if (k < n-1) :
        print()