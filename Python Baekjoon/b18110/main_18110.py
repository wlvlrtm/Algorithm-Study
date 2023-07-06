## solved.ac
import sys

def round(num) :
    if (num - int(num) >= 0.5) :
        return int(num) + 1
    else :
        return int(num)

n = int(sys.stdin.readline())
l = list()
per = round(n * 0.15)

if (n == 0) :
    print(0)
else :
    for _ in range(n) :
        l.append(int(sys.stdin.readline()))

    l.sort()

    if (per != 0) :
        l = l[per:-per]

    print(round(sum(l)/len(l)))