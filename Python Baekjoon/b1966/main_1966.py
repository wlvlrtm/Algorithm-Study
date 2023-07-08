## 프린터 큐
import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t) :
    n, m = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    index = deque(list(i for i in range(len(queue))))
    counter = 0

    while (queue) :
        mx = max(queue)

        while (queue[0] != mx) :
            queue.append(queue.popleft())
            index.append(index.popleft())
        else :
            counter += 1

        if (index[0] == m) :
            break
        else :
            queue.popleft()
            index.popleft()

    print(counter)