## 이항 계수 1
n, r = map(int, input().split())

ni = n
ri = r
nri = (n - r)

if (r == 0 or r == n) :
    print(1)
else :
    for i in range(1, n) :
        ni *= i

    for j in range(1, r) :
        ri *= j

    for k in range(1, nri) :
        nri *= k

    print(ni // (ri * nri))