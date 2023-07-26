## 계단 오르기
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    s = list()
    d = [0] * (n)

    for _ in range(n) :
        s.append(int(sys.stdin.readline().strip()))

    if (n <= 2) :
        print(sum(s))
    else :  ## 계단이 3개 이상
        d[0] = s[0]
        d[1] = s[0] + s[1]

        for i in range(2, n) :
            d[i] = max(d[i - 3] + s[i - 1] + s[i], d[i - 2] + s[i]) ## 1개 밟고, 1개 생략, 2개 연속 or 2개 연속, 1개 생략, 1개 밟기

        print(d[n-1])



if (__name__ == "__main__") :
    main()