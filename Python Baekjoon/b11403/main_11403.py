## 경로 찾기
import sys
from collections import deque

global n, visited

def main() :
    global n, visited

    n = int(sys.stdin.readline().strip())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(0, n) :
        bfs(graph, i)

    for i in visited :
        print(*i)

def bfs(graph, x):
    global n, visited

    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1



if (__name__ == "__main__") :
    main()