## 미로 탐색
import sys
from collections import deque

global n, m

def main() :
    global n, m

    n, m = map(int, sys.stdin.readline().split())
    table = []

    for _ in range(n) :
        table.append(list(map(int, sys.stdin.readline().rstrip())))

    bfs(table, (0, 0))

def bfs(table, v) :
    global n, m

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((v[0], v[1]))

    while (queue) :
        x, y = queue.popleft()

        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y

            if (0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1) :
                queue.append((nx, ny))
                table[nx][ny] = table[x][y] + 1

    print(table[n - 1][m - 1])



if (__name__ == "__main__") :
    main()