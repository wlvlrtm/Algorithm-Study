## DFS와 BFS
import sys
from collections import deque

global dfs_visited
global bfs_visited
global graph
global n

def main() :
    global dfs_visited, bfs_visited, graph, n

    n, m, v = map(int, sys.stdin.readline().split())    # node, line, start node
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for _ in range(m) :
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = True
        graph[y][x] = True

    dfs_visited = [False] * (n + 1)
    bfs_visited = [False] * (n + 1)

    dfs(v)
    print()
    bfs(v)

def dfs(v) :
    global dfs_visited, graph, n

    dfs_visited[v] = True
    print(v, end = " ")

    for i in range(1, n + 1) :
        if (dfs_visited[i] == False and graph[v][i] == True) :
            dfs(i)

def bfs(v) :
    global bfs_visited, graph, n

    queue = deque([v])
    bfs_visited[v] = True

    while (queue) :
        v = queue.popleft()
        print(v, end = " ")

        for i in range(1, n + 1) :
            if (bfs_visited[i] == False and graph[v][i]) :
                queue.append(i)
                bfs_visited[i] = True



if (__name__ == "__main__") :
    main()