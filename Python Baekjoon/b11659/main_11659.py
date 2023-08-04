## 구간 합 구하기 4
import sys

def main() :
    n, m = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    sum_l = [0]
    t = 0

    for i in l :
        t += i
        sum_l.append(t)

    for _ in range(m) :
        i, j = map(int, sys.stdin.readline().split())
        print(sum_l[j] - sum_l[i-1])



if (__name__ == "__main__") :
    main()