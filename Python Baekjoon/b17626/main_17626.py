## Four Squares
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    dp = [0, 1]

    for i in range(2, n + 1) :
        v = 999999999
        j = 1

        while ((j ** 2) <= i) :
            v = min(v, dp[i - (j ** 2)])
            j += 1

        dp.append(v + 1)

    print(dp[n])



if (__name__ == "__main__") :
    main()