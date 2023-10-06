## 테트로미노
import sys

global n, m, mxx, direction, visited, table

def main() :
    global n, m, mxx, direction, visited, table

    n, m = map(int, sys.stdin.readline().split())

    mxx = 0
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            visited[i][j] = True
            dfs_4((i, j), table[i][j], 1)
            visited[i][j] = False
            dfs_1((i, j))

    print(mxx)


def dfs_4(v, temp_sum, count) :   ## (ㅗ, ㅓ, ㅏ, ㅜ) 제외 나머지 테트로미노
    global n, m, mxx, direction, visited, table

    if (count == 4) :
        mxx = max(mxx, temp_sum)
        return

    for i in range(4) : ## 상, 하, 좌, 우
        nx = v[0] + direction[i][0]
        ny = v[1] + direction[i][1]

        if (0 <= nx < n and 0 <= ny < m) :
            if not (visited[nx][ny]) :
                visited[nx][ny] = True
                dfs_4((nx, ny), temp_sum + table[nx][ny], count + 1)
                visited[nx][ny] = False

def dfs_1(v) :
    global n, m, mxx, direction, visited, table

    for i in range(4) :
        tmp = table[v[0]][v[1]]

        for j in range(3) :
            t = (i + j) % 4
            nx = v[0] + direction[t][0]
            ny = v[1] + direction[t][1]

            if not (0 <= nx < n and 0 <= ny < m) :
                tmp = 0
                break

            tmp += table[nx][ny]

        mxx = max(mxx, tmp)



if (__name__ == "__main__") :
    main()