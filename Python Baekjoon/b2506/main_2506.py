## 바이러스
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    s = int(sys.stdin.readline().strip())
    g = [[] for i in range(n + 1)]
    v = [0] * (n + 1)

    for _ in range(s) :
        a, b = map(int, sys.stdin.readline().split())
        g[a] += [b]
        g[b] += [a]
    


if (__name__ == "__main__") :
    main()