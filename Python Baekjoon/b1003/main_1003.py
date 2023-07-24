## 피보나치 함수
import sys

def fibonacci(n : int) :
    


def main() :
    t = int(sys.stdin.readline().strip())
    l = list()

    for _ in range(t) :
        l.append(int(sys.stdin.readline().strip()))

    for i in l :
        fibonacci(i)



if (__name__ == "__main__") :
    main()