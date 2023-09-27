## 적록색약
import sys
sys.setrecursionlimit(1000000)

global n, visited, rgb, oob

def main():
    global n, visited, rgb, oob, table

    n = int(sys.stdin.readline().strip())
    table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    rgb, oob = 0, 0

    for i in range(n) :
        for j in range(n) :
            if (visited[i][j] == False) :
                dfs(i, j)
                rgb += 1

    for i in range(n) :
        for j in range(n) :
            if (table[i][j] == 'R') :
                table[i][j] = 'G'

    visited = [[False] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if (visited[i][j] == False) :
                dfs(i, j)
                oob += 1

    print(rgb, oob)


def dfs(x, y) :
    global n, visited, rgb, oob

    visited[x][y] = True
    color = table[x][y]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False) :
            if (table[nx][ny] == color) :
                dfs(nx, ny)



if (__name__ == "__main__") :
    main()