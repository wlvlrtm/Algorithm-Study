## 직사각형에서 탈출
x, y, w, h = map(int, input().split())
print(min(x, y, (h-y), (w-x)))