## 좌표 정렬하기
import sys
n = int(sys.stdin.readline())
l = list()

for _ in range(n) :
    x, y = map(int, input().split())
    l.append((x, y))

l.sort()

for i in l :
    print(i[0], i[1])