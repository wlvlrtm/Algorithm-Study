## 약수 구하기
n, k = map(int, input().split())
r = list()

for i in range(1, n+1) :
    if (n % i == 0) :
        r.append(i)

try :
    print(r[k-1])
except :
    print(0)