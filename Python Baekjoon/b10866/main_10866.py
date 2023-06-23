## 덱
import sys
from collections import deque

n = int(sys.stdin.readline())
d = deque()

for _ in range(n) :
    x = sys.stdin.readline().split()
    if (x[0] == "push_front") :
        d.appendleft(x[1])
    elif (x[0] == "push_back") :
        d.append(x[1])
    elif (x[0] == "pop_front") :
        if (len(d) > 0) :
            print(d.popleft())
        else :
            print(-1)
    elif (x[0] == "pop_back") :
        if (len(d) > 0) :
            print(d.pop())
        else :
            print(-1)
    elif (x[0] == "size") :
        print(len(d))
    elif (x[0] == "empty") :
        if (len(d) > 0) :
            print(0)
        else :
            print(1)
    elif (x[0] == "front") :
        if (len(d) > 0) :
            print(d[0])
        else :
            print(-1)
    elif (x[0] == "back") :
        if (len(d) > 0) :
            print(d[-1])
        else :
            print(-1)