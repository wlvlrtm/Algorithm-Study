## 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)

global visited
global graph
global n
global r

def main() :
    global visited, graph, n, r

    r = 0
    n, m = map(int, sys.stdin.readline().split())
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m) :
        u, v = map(int, sys.stdin.readline().split())
        graph[u][v] = True
        graph[v][u] = True

    for i in range(1, n + 1) :
        if (visited[i] == False) :
            dfs(i)
            r += 1

    print(r)

def dfs(v) :
    global visited, graph, n, r

    visited[v] = True

    for i in range(1, n + 1) :
        if (visited[i] == False and graph[v][i] == True) :
            if (graph[i][v] == True) :
                dfs(i)
            else :
                break



if (__name__ == "__main__") :
    main()