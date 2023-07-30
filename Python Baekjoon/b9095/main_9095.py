## 1, 2, 3 더하기
import sys

def sum(n: int) -> int :
    if (n > 3) :
        return sum(n - 1) + sum(n - 2) + sum(n - 3)
    elif (n == 1) :
        return 1
    elif (n == 2) :
        return 2
    elif (n == 3) :
        return 4

def main() :
    t = int(sys.stdin.readline().strip())
    l = list()

    for _ in range(t) :
        n = int(sys.stdin.readline().strip())
        l.append(sum(n))

    for i in l :
        print(i)



if (__name__ == "__main__") :
    main()