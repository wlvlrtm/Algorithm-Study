## 큐
import sys

n = int(sys.stdin.readline())
l = list()

for _ in range(n) :
    x = sys.stdin.readline().split()

    if (x[0] == "push") :
        l.append(x[1])
    elif (x[0] == "pop") :
        if (len(l) > 0) :
            print(l.pop(0))
        else :
            print(-1)
    elif (x[0] == "size") :
        print(len(l))
    elif (x[0] == "empty") :
        if (len(l) == 0) :
            print(1)
        else :
            print(0)
    elif (x[0] == "front") :
        if (len(l) > 0) :
            print(l[0])
        else :
            print(-1)
    elif (x[0] == "back") :
        if (len(l) > 0) :
            print(l[-1])
        else :
            print(-1)