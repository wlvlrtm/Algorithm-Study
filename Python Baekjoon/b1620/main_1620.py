## 나는야 포켓몬 마스터 이다솜
import sys

def main() :
    n, m = map(int, sys.stdin.readline().split())
    ig = dict()

    for i in range(1, n + 1) :   ## Add
        val = sys.stdin.readline().strip()
        ig[i] = val
        ig[val] = i

    for j in range(m) : ## Question
        q = sys.stdin.readline().strip()

        if (q.isdigit()) :
            print(ig[int(q)])
        else :
            print(ig[q])



if (__name__ == "__main__") :
    main()