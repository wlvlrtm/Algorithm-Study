## 최대 힙
import sys
import heapq


def main() :
    n = int(sys.stdin.readline().strip())
    heap = []

    for _ in range(n) :
        x = int(sys.stdin.readline().strip())

        if (x) :
            heapq.heappush(heap, (-x, x))
        else :
            if (len(heap) >= 1) :
                print(heapq.heappop(heap)[1])
            else :
                print(0)



if (__name__ == "__main__") :
    main()