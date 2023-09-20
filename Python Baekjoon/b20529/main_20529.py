## 가장 가까운 세 사람의 심리적 거리
import sys

def main() :
    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        n = int(sys.stdin.readline().strip())
        mbti = sys.stdin.readline().split()
        ans = 999999

        if (n <= 32) :
            for a in range(n) :
                for b in range(n) :
                    for c in range(n) :
                        count = 0

                        if (a == b or b == c or a == c) :
                            continue
                        else :
                            for i in range(4) :
                                if (mbti[a][i] != mbti[b][i]) :
                                    count += 1
                                if (mbti[a][i] != mbti[c][i]) :
                                    count += 1
                                if (mbti[b][i] != mbti[c][i]) :
                                    count += 1

                        ans = min(count, ans)
        else :
            ans = 0

        print(ans)


if (__name__ == "__main__") :
    main()