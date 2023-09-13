## 바이러스
import sys

def spread_virus(node, graph, visited) :
    visited[node] = 1

    for i in graph[node] :
        if not (visited[i] == 1) :
            spread_virus(i, graph, visited)

def main() :
    n = int(sys.stdin.readline().strip())
    s = int(sys.stdin.readline().strip())
    graph = [[] for i in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(s) :
        a, b = map(int, sys.stdin.readline().split())
        graph[a] += [b]
        graph[b] += [a]

    spread_virus(1, graph, visited)

    print(visited.count(1) - 1)
    


if (__name__ == "__main__") :
    main()