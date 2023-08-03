## 파도반 수열
import sys

def main() :
    t = int(sys.stdin.readline().strip())
    p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    r = list()

    for i in range(11, 101) :
        p.append(p[i - 3] + p[i - 2])

    for _ in range(t) :
        n = int(sys.stdin.readline().strip())
        r.append(p[n])

    for i in r :
        print(i)



if (__name__ == "__main__") :
    main()