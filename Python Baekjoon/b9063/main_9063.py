## 대지
n = int(input())
la = list()
lb = list()

for i in range(0, n) :
    a, b = map(int, input().split())
    la.append(a)
    lb.append(b)

x = max(la) - min(la)
y = max(lb) - min(lb)

print(x*y)