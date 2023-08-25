## 숨바꼭질
import sys
from collections import deque

global n, k, dst, mxx

def main() :
    global n, k, dst, mxx

    n, k = map(int, sys.stdin.readline().split())
    mxx = 10 ** 5
    dst = [0] * (mxx + 1)

    print(bfs(n))

def bfs(v) :
    global n, k, dst, mxx

    q = deque()
    q.append(v)

    while (q) :
        x = q.popleft()

        if (x == k) :
            return (dst[x])

        for i in (x - 1, x + 1, x * 2) :
            if (0 <= i <= mxx and not dst[i]) :
                dst[i] = dst[x] + 1
                q.append(i)



if (__name__ == "__main__") :
    main()