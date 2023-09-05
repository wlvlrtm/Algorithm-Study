## 헌내기는 친구가 필요해
import sys
sys.setrecursionlimit(10**6)

global visited
global count
global n, m

def main() :
    global visited
    global n, m
    global count

    n, m = map(int, sys.stdin.readline().split())   ## 3, 5
    count = 0
    table = [[] for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    v = ()

    for i in range(n) : ## O: 빈 공간, X: 벽, I: 도연이, P: 사람
        table[i] = [*sys.stdin.readline().strip()]

        for j in range(m) :
            if (table[i][j] == 'I') :
                v = (i, j)

    dfs(table, v)

    if (count == 0) :
        print("TT")
    else :
        print(count)


def dfs(table, v) :
    global visited
    global n, m
    global count

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    if (0 <= v[0] < n and 0 <= v[1] < m) :
        if (visited[v[0]][v[1]] == 0) :
            visited[v[0]][v[1]] = 1

            if (table[v[0]][v[1]] == 'P') :
                count += 1

            for i in range(4) :
                nx, ny = v[0] + dx[i], v[1] + dy[i]

                if (0 <= nx < n and 0 <= ny < m) :
                    if (visited[nx][ny] == 0) :
                        if (table[nx][ny] != 'X') :
                            dfs(table, (nx, ny))



if (__name__ == "__main__") :
    main()