## 커트라인
import sys

def main() :
    n, k = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))

    l.sort(reverse = True)

    print(l[k - 1])



if (__name__ == "__main__") :
    main()