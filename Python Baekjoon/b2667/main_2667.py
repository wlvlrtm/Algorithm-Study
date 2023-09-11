## 단지번호붙이기
import sys
from collections import deque

global n

def main() :
    global n

    n = int(sys.stdin.readline().strip())
    table = []
    arr = []

    for _ in range(n) :
        table.append(list(map(int, sys.stdin.readline().rstrip())))

    for i in range(n) :
        for j in range(n) :
            if (table[i][j] == 1) :
                arr.append(bfs(table, (i, j)))

    arr.sort()

    print(len(arr))

    for i in range(len(arr)) :
        print(arr[i])

def bfs(table, v) :
    global n

    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append(v)

    table[v[0]][v[1]] = 0

    while (queue) :
        x, y = queue.popleft()

        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y

            if (0 <= nx < n and 0 <= ny < n and table[nx][ny] == 1) :
                table[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count



if (__name__ == "__main__") :
    main()