## 공 바꾸기
n, m = map(int, input().split())
l = [0] * n

for a in range(1, n+1) :
    l[a-1] = a

for b in range(0, m) :
    i, j = map(int, input().split())
    l[i-1], l[j-1] = l[j-1], l[i-1]

for c in l :
    print(c, end=" ")