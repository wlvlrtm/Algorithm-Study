## 킹, 퀸, 룩, 비숍, 나이트, 폰
la = [1, 1, 2, 2, 2, 8]
lb = list(map(int, input().split()))
lc = [a - b for a, b in zip(la, lb)]

for i in lc :
    print(i, end=" ")