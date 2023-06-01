## 세 막대
a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()

while (l[2] >= l[0] + l[1]) :
    l[2] -= 1

print(l[0] + l[1] + l[2])