## 스택 수열
import sys

n = int(sys.stdin.readline())
l = list()
stk = []
cur = 1
r = list()

for _ in range(n) :
    num = int(sys.stdin.readline())

    while (cur <= num) :
        stk.append(cur)
        r.append('+')
        cur += 1

    if (stk[-1] == num) :
        stk.pop()
        r.append('-')
    else :
        print("NO")
        cur = -1
        break

if (cur != -1) :
    for i in r :
        print(i)