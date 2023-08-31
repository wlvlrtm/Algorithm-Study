## 쉬운 최단거리
import sys
from collections import deque

global visited
global distance
global n, m

def bfs(table, v) :
    global visited
    global distance
    global n, m

    queue = [v]
    step_row = [1, 0, -1, 0]
    step_column = [0, 1, 0, -1]
        ## (+1, 0) : move right
        ## (-1, 0) : move left
        ## (0, +1) : move up
        ## (0, -1) : move down

    visited[v[0]][v[1]] = 1
    distance[v[0]][v[1]] = 0

    while (queue) :
        cn, cm = queue.pop(0)

        for i in range(4) :
            r, c = cn + step_row[i], cm + step_column[i]

            if (0 <= r < n and 0 <= c < m and visited[r][c] == 0) :
                if (table[r][c] == 1) :
                    distance[r][c] = distance[cn][cm] + 1
                    visited[r][c] = 1
                    queue.append([r, c])
                elif (table[r][c] == 0) :
                    distance[r][c] = 0

def main() :
    global visited
    global distance
    global n, m

    n, m = map(int, sys.stdin.readline().split())   ## n = 세로 // m = 가로

    table = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    pos = ()

    for i in range(n) :             ## i = 0
        input_row = list(map(int, sys.stdin.readline().split()))    ## 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
                                                                    ## (0, 0), (0, 1) ~ (0, 14)
        for j in range(len(input_row)) :
            if (input_row[j] == 2) :
                pos = (i, j)        ## (0, 0)

        table.append(input_row)     ## table = [ [2 1 1 1 1 1 1 1 1 1 1 1 1 1 1] ]

    bfs(table, pos)

    for i in range(n) :
        for j in range(m) :
            if (distance[i][j] == -1 and table[i][j] == 0) :
                distance[i][j] = 0

    for k in distance :
        print(*k)   ## unpacking



if (__name__ == "__main__") :
    main()