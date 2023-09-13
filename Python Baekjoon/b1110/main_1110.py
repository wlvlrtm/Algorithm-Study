## 더하기 사이클
import sys

def main() :
    count = 0

    n = int(sys.stdin.readline().strip())
    n1 = n

    while (True) :
        t = ((n % 10) * 10) + (((n // 10) + (n % 10)) % 10)
        n = t
        count += 1

        if (n1 == n) :
            print(count)
            break



if (__name__ == "__main__") :
    main()