## 리모컨
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    count = abs(100 - n)

    if (m > 0) :
        broken = set(sys.stdin.readline().split())
    else :
        broken = set()

    for i in range(1000001) :
        for j in str(i) :
            if j in broken :
                break
        else :
            count = min(count, len(str(i)) + abs(i - n))

    print(count)



if (__name__ == "__main__") :
    main()