## 뱀과 사다리 게임
import sys
from collections import deque

global n, m, visited, table, ladder, snake

def main() :
    global n, m, visited, table, ladder, snake

    n, m = map(int, sys.stdin.readline().split())

    visited = [False] * 101
    table = [0] * 101
    ladder = dict()
    snake = dict()


    for _ in range(n) :
        x, y = map(int, sys.stdin.readline().split())
        ladder[x] = y

    for _ in range(m) :
        u, v = map(int, sys.stdin.readline().split())
        snake[u] = v

    bfs(1)


def bfs(v) :
    global n, m, visited, table, ladder, snake

    q = deque([v])
    dice = [1, 2, 3, 4, 5, 6]

    while (q) :
        x = q.popleft()

        if (x == 100) : ## Finish!
            print(table[x])
            break
        else :
            for i in dice :
                nx = x + i
                if (1 <= nx <= 100) :
                    if (nx in ladder.keys()) :
                        nx = ladder[nx]
                    elif (nx in snake.keys()) :
                        nx = snake[nx]

                    if (visited[nx] == False) :
                        visited[nx] = True
                        table[nx] = table[x] + 1

                        q.append(nx)



if (__name__ == "__main__") :
    main()