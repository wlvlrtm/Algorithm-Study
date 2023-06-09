## 최대공약수와 최소공배수
a, b = map(int, input().split())
la = [1, a]
lb = [1, b]

for i in range(2, a) :
    if (a % i == 0) :
        la.append(i)

for j in range(2, b) :
    if (b % j == 0) :
        lb.append(j)

la.sort()
lb.sort()

sa = set(la)
sb = set(lb)

t = sa.intersection(sb)

print(max(list(t)))
print((a*b) // max(list(t)))