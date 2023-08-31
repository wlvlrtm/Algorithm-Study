## 토마토
import sys
from collections import deque

global m, n
global visited
global queue

def main() :
    global m, n
    global visited
    global queue

    m, n = map(int, sys.stdin.readline().split())
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    queue = deque([])

    for i in range(n) :
        for j in range(m) :
            if (box[i][j] == 1) :
                queue.append([i, j])

    bfs(box)

def bfs(box) :
    global m, n
    global visited
    global queue

    day = 0
    dir_row = [-1, 1, 0, 0]
    dir_col = [0, 0, -1, 1]

    while (queue) :
        col, row = queue.popleft()

        for i in range(4) :
            next_row, next_col = row + dir_row[i], col + dir_col[i]

            if (0 <= next_col < n and 0 <= next_row < m and box[next_col][next_row] == 0) :
                box[next_col][next_row] = box[col][row] + 1
                queue.append([next_col, next_row])

    for i in box :
        for j in i :
            if (j == 0) :
                print(-1)
                exit(0)

        day = max(day, max(i))

    print(day - 1)



if (__name__ == "__main__") :
    main()