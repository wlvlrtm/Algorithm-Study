## 수 정렬하기 2
import sys

n = int(sys.stdin.readline())
l = list()

for _ in range(n) :
    l.append(int(sys.stdin.readline()))

l.sort()

for i in l :
    print(i)