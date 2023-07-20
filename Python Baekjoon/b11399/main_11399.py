## ATM
import sys

def main() :
    n = int(sys.stdin.readline())
    a = 0
    r = 0
    pi = list((map(int, sys.stdin.readline().split())))

    pi.sort()

    for i in pi :
        a = (i + a)
        r += a

    print(r)



if (__name__ == "__main__") :
    main()