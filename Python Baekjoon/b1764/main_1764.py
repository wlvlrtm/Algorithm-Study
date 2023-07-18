## 듣보잡
import sys

def main() :
    n, m = map(int, sys.stdin.readline().split())
    s = set()
    r = list()

    for i in range(n) :
        ln = sys.stdin.readline().strip()
        s.add(ln)

    for j in range(m) :
        vn = sys.stdin.readline().strip()

        if (vn in s) :
            r.append(vn)
        else :
            s.add(vn)

    print(len(r))

    for k in sorted(r) :
        print(k)



if (__name__ == "__main__") :
    main()