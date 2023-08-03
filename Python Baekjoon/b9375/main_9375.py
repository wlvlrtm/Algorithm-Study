## 패션왕 신해빈
import sys


def main() :
    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        n = int(sys.stdin.readline().strip())
        d = dict()

        for _ in range(n) :
            cloth, type = map(str, sys.stdin.readline().strip().split())

            if (d.get(type) == None) :
                d[type] = set()

            d[type].add(cloth)

        r = 1

        for key in d.keys() :
            r *= (len(d[key]) + 1)

        print(r - 1)



if (__name__ == "__main__") :
    main()