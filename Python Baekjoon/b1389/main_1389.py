## 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

global n, m
global visited

def main() :
    global n, m
    global visited

    result = []
    n, m = map(int, sys.stdin.readline().split())   ## n: 유저의 수 // m: 친구 관계의 수
    graph = [[] * n for _ in range(n + 1)]

    for _ in range(m) :
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1) :
        result.append(bfs(graph, i))

    print(result.index(min(result)) + 1)

def bfs(graph, v) :
    global n, m
    global visited

    queue = deque()
    step = [0] * (n + 1)
    visited = [v]

    queue.append(v)

    while (queue) :
        x = queue.popleft()

        for i in graph[x] :
            if (i not in visited) :
                step[i] = (step[x] + 1)
                visited.append(i)
                queue.append(i)

    return sum(step)



if (__name__ == "__main__") :
    main()