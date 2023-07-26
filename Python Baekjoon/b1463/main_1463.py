## 1로 만들기
import sys

def main() :
    x = int(sys.stdin.readline().strip())
    d = [0] * (x + 1)   ## i가 1이 되는데 필요한 연산의 횟수 저장; 1이 1이 되는데 필요한 연산 == 0, 2가 1이 되는데 필요한 연산 == 1 ~

    for i in range(2, x + 1) :
        d[i] = (d[i - 1] + 1)

        if (i % 2 == 0) :
            d[i] = min(d[i], d[i // 2] + 1)

        if (i % 3 == 0) :
            d[i] = min(d[i], d[i // 3] + 1)

    print(d[x])



if (__name__ == "__main__") :
    main()