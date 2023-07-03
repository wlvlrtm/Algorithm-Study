## 좌표 정렬하기 2
import sys

n = int(sys.stdin.readline())
l = list()

for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    l.append((x, y))

l.sort(key=lambda x : (x[1], x[0]))

for i in l :
    print(i[0], i[1])