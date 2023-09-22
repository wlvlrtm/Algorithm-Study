## AC
import sys
from collections import deque

def main() :
    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        p = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        l = sys.stdin.readline().strip()

        count = 0
        result = 0

        if (n == 0) :
            q = deque()
        else :
            q = deque(l[1: -1].split(','))

        for i in range(len(p)) :
            if (p[i] == 'R') :
                count += 1
            elif (p[i] == 'D') :
                if (len(q) == 0) :
                    print("error")
                    result = -1
                    break
                else :
                    if (count % 2 == 0) :
                        q.popleft()
                    else :
                        q.pop()

        if (result == -1) :
            continue
        else :
            if not (count % 2 == 0) :
                q.reverse()

            print('[' + ','.join(q) + ']')



if (__name__ == "__main__") :
    main()