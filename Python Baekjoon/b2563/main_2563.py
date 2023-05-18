## 색종이
n = int(input())
lx = list()
t = (100 * n)

for i in range(0, n) :
    x, y = map(int, input().split())
    px = [x, x + 10]
    lx.append(px)

print(lx)

## a < c < b < d
## c < a < d < b