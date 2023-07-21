## 수 정렬하기
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    r = list()

    for _ in range(n) :
        r.append(int(sys.stdin.readline().strip()))

    r.sort()

    for i in r :
        print(i)


if (__name__ == "__main__") :
    main()