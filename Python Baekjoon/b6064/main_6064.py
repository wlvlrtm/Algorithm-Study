## 카잉 달력
import sys

def main() :
    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        m, n, x, y = map(int, sys.stdin.readline().split()) ## m = 10, n = 12
        f = -1

        while (x <= m * n) :
            if (x % n == y % n) :
                print(x)
                f = 0
                break
            x += m

        if (f == -1) :
            print(f)


if (__name__ == "__main__") :
    main()