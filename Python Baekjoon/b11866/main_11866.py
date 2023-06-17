## 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
q = deque()
r = list()

for i in range(1, n+1) :
    q.append(i)

while (len(q) > 0) :
    for j in range(k-1) :
        q.append(q.popleft())
    r.append(q.popleft())

print("<", end="")

for k in range(len(r)-1) :
    print(f"{r[k]}, ", end="")

print(f"{r[-1]}", end="")
print(">")