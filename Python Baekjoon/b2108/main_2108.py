## 통계학
import sys

n = int(sys.stdin.readline())
l = list()

for _ in range(n) :
    l.append(int(sys.stdin.readline()))

l.sort()

print(round(sum(l) / len(l)))
print(l[len(l) // 2])

dic = dict()

for i in l :
    if (i in dic) :
        dic[i] += 1
    else :
        dic[i] = 1

mx = max(dic.values())
lm = list()

for j in dic :
    if (mx == dic[j]) :
        lm.append(j)

if (len(lm) > 1) :
    print(lm[1])
else :
    print(lm[0])

print(abs(min(l) - max(l)))