## IOIOI
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    r, c, i = 0, 0, 0

    for _ in range(m) :
        if (s[i : i + 3] == "IOI") :
            i = i + 2
            c += 1

            if (c == n) :   ## correct!
                r += 1
                c -= 1

        else :
            i += 1
            c = 0

    print(r)



if (__name__ == "__main__") :
    main()