## 바구니 뒤집기
n, m = map(int, input().split())
l = [i for i in range(1, n+1)]

for a in range(0, m) :
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    k = i
    for b in list(reversed(l[i:j+1])) :
        l[k] = b
        k += 1


for c in l :
    print(c, end=" ")