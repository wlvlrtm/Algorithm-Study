## 유기농 배추
import sys
from collections import deque

m, n, k = 0, 0, 0
field = [0][0]

def bfs(x, y) :
    global m, n, k, field

    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    q = deque()
    q.append((x, y))

    while (q) :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= m) :
                continue

            if (field[nx][ny] == 1) :
                q.append((nx, ny))
                field[nx][ny] = 0

def main() :
    global m, n, k, field
    t = int(sys.stdin.readline().strip())   ## test case

    for _ in range(t) :
        m, n, k = map(int, sys.stdin.readline().split())    ## width, height, num
        field = [[0 for _ in range(m)] for _ in range(n)]
        r = 0

        for _ in range(k) : ## 배추 심기
            x, y = map(int, sys.stdin.readline().split())   ## pos (x, y)
            field[y][x] = 1

        for i in range(n) :
            for j in range(m) :
                if (field[i][j] == 1) :
                    bfs(i, j)
                    r += 1

        print(r)


if (__name__ == "__main__") :
    main()