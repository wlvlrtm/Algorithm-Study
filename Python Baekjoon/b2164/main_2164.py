## 카드 2
from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque([i for i in range(1, n+1)])
i = 1

while (len(q) > 1 and n != 1) :
    q.popleft()
    i = q.popleft()
    q.append(i)

print(i)