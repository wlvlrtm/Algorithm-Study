## 피보나치 함수
import sys

z = [1, 0, 1]
o = [0, 1, 1]

def fibonacci(n : int) :
    l = len(z)

    if (n >= l) :
        for i in range(l, n + 1) :
            z.append(z[i - 1] + z[i - 2])
            o.append(o[i - 1] + o[i - 2])

    print(z[n], o[n])

def main() :
    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        fibonacci(int(sys.stdin.readline().strip()))



if (__name__ == "__main__") :
    main()