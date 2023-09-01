## 나무 자르기
import sys

def main() :
    n, m = map(int, sys.stdin.readline().split())   ## 4, 7 (n: 개수 // m: 길이)
    trees = list(map(int, sys.stdin.readline().split()))

    start = 1
    end = max(trees)

    while (start <= end) :
        target = (start + end) // 2
        length = 0

        for i in trees :
            if (i >= target) :
                length += (i - target)

        if (length >= m) :
            start = (target + 1)
        else :
            end = (target - 1)

    print(end)



if (__name__ == "__main__") :
    main()