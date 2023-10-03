## 토마토
import sys
from collections import deque

global m, n, h
global queue

def main() :
    global m, n, h
    global queue

    m, n, h = map(int, sys.stdin.readline().split())    ## 가로, 세로, 높이

    queue = deque([])
    table = []

    for i in range(h) :
        tmp = []

        for j in range(n) :
            tmp.append(list(map(int, sys.stdin.readline().split())))  ## 1: 익음, 0: 안 익음, -1: 없음

            for k in range(m) :
                if (tmp[j][k] == 1) :
                    queue.append([i, j, k])

        table.append(tmp)

    bfs(table)


def bfs(table) :
    global m, n, h
    global queue

    day = 0
    dir_x = [-1, 1, 0, 0, 0, 0]
    dir_y = [0, 0, -1, 1, 0, 0]
    dir_z = [0, 0, 0, 0, -1, 1]

    while (queue) :
        x, y, z = queue.popleft()

        for i in range(6) :
            next_x = dir_x[i] + x
            next_y = dir_y[i] + y
            next_z = dir_z[i] + z

            if (0 <= next_x < h and
                0 <= next_y < n and
                0 <= next_z < m and
                table[next_x][next_y][next_z] == 0) :
                queue.append([next_x, next_y, next_z])
                table[next_x][next_y][next_z] = table[x][y][z] + 1


    for i in table :
        for j in i :
            for k in j :
                if (k == 0) :   ## Fail
                    print(-1)
                    exit(0)

            day = max(day, max(j))

    print(day - 1)



if (__name__ == "__main__") :
    main()