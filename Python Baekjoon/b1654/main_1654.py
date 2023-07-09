## 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
l = list()

for _ in range(k) :
    l.append(int(sys.stdin.readline()))

mn = 1
mx = max(l)

while (mn <= mx) :
    md = ((mn + mx) // 2)
    ct = 0

    for i in l :
        ct += (i // md)

    if (ct >= n) :
        mn = (md + 1)
    else :
        mx = (md - 1)

print(mx)