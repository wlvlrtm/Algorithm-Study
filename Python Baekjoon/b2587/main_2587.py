## 대표값 2
import sys

def main() :
    l = list()
    avg = 0
    mid = 0

    for _ in range(5) :
        l.append(int(sys.stdin.readline().strip()))

    l.sort()

    avg = (sum(l) // len(l))
    mid = l[2]

    print(avg)
    print(mid)



if (__name__ == "__main__") :
    main()