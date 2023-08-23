## 좌표 압축
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    dict = {}

    lu = list(map(int, sys.stdin.readline().split()))
    ls = list(set(lu))
    ls.sort()

    for i in range(len(ls)) :
        dict[ls[i]] = i

    for j in lu :
        print(dict[j], end = " ")



if (__name__ == "__main__") :
    main()