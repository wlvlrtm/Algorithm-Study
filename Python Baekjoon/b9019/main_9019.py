## DSLR
import sys
from collections import deque

global a, b, visited

def main() :
    global a, b, visited

    t = int(sys.stdin.readline().strip())

    for _ in range(t) :
        a, b = map(int, sys.stdin.readline().rstrip().split())

        visited = [False for i in range(10001)]
        q = deque()

        q.append([a, ''])
        visited[a] = True

        bfs(q)


def bfs(q) :
    global a, b, visited

    while (q):
        num, command = q.popleft()

        d = (num * 2) % 10000
        s = (num - 1) % 10000
        l = (num // 1000) + (num % 1000) * 10
        r = num // 10 + (num % 10) * 1000

        if (num == b) :
            print(command)
            break

        if not (visited[d]) :
            visited[d] = True
            q.append([d, command + 'D'])

        if not (visited[s]) :
            visited[s] = True
            q.append([d, command + 'S'])

        if not (visited[l]) :
            visited[l] = True
            q.append([l, command + 'L'])

        if not (visited[r]) :
            visited[r] = True
            q.append([r, command + 'R'])



if (__name__ == "__main__") :
    main()