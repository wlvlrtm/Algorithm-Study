## 수 정렬하기 3
import sys

r = [0] * 10001

for _ in range(int(sys.stdin.readline())) :
    r[int(sys.stdin.readline())] += 1

for j in range(1, len(r)) :
    if (r[j] != 0) :
        for _ in range(0, r[j]) :
            print(j)