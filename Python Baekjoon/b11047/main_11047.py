## 동전 0
import sys

def main() :
    n, k = map(int, sys.stdin.readline().split())
    a = list()
    r = 0

    for _ in range(n) :
        a.append(int(sys.stdin.readline()))

    for i in range(n - 1, -1, -1) :
        r += (k // a[i])
        k = (k % a[i])

    print(r)



if (__name__ == "__main__") :
    main()