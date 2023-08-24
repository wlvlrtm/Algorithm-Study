## Z
import sys

def main() :
    n, r, c = map(int, sys.stdin.readline().split())
    a = 0

    while (n != 0) :
        n -= 1

        if (r < 2 ** n and c < 2 ** n) :
            a += (2 ** n) * (2 ** n) * 0
        elif (r < 2 ** n and c >= 2 ** n) :
            a += (2 ** n) * (2 ** n) * 1
            c -= (2 ** n)
        elif (r >= 2 ** n and c < 2 ** n) :
            a += (2 ** n) * (2 ** n) * 2
            r -= (2 ** n)
        else :
            a += (2 ** n) * (2 ** n) * 3
            r -= (2 ** n)
            c -= (2 ** n)

    print(a)



if (__name__ == "__main__") :
    main()