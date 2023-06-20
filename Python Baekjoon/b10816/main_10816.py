## 숫자 카드 2
n = int(input())
a = map(int, input().split())
m = int(input())
b = map(int, input().split())
r = list()
h = {}

for i in a :
    if (i in h) :
        h[i] += 1
    else :
        h[i] = 1

for j in b :
    if (j in h) :
        r.append(f"{h[j]}")
    else :
        r.append("0")

print(" ".join(r))