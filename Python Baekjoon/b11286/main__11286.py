## 절댓값 힙
import sys
import heapq

def main() :
    heap = []

    n = int(sys.stdin.readline().strip())

    for _ in range(n) :
        x = int(sys.stdin.readline().strip())

        if (x != 0) :
            heapq.heappush(heap, (abs(x), x))
        else :
            try :
                print(heapq.heappop(heap)[1])
            except :
                print(0)



if (__name__ == "__main__") :
    main()