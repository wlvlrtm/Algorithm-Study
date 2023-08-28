## 회의실 배정
import sys

def main() :
    n = int(sys.stdin.readline().strip())

    lst = [[0] * 2 for _ in range(n)]

    for i in range(n) :
        st, et = map(int, sys.stdin.readline().split())

        lst[i][0] = st
        lst[i][1] = et

    lst.sort(key = lambda x: (x[1], x[0]))

    r = 1
    et = lst[0][1]

    for i in range(1, n) :
        if (lst[i][0] >= et) :
            r += 1
            et = lst[i][1]

    print(r)

if (__name__ == "__main__") :
    main()