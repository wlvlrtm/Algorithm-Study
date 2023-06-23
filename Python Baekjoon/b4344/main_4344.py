## 평균은 넘겠지
import sys

c = int(sys.stdin.readline())

for _ in range(c) :
    r = 0
    n = list(map(int, sys.stdin.readline().split()))
    a = sum(n[1:]) / n[0]

    for i in n[1:] :
        if (i > a) :
            r += 1

    r = (r / n[0]) * 100
    r = round(r + 10 ** (-len(str(r)) - 1), 3)
    print(f"{r:.3f}%")