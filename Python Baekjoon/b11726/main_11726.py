## 2xn 타일링
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    l = [0] * 1001

    l[1] = 1
    l[2] = 2

    for i in range(3, 1001) :
        l[i] = (l[i - 1] + l[i - 2]) % 10007

    print(l[n])


if (__name__ == "__main__") :
    main()