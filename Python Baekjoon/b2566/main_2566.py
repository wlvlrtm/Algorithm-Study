## 최댓값
t = list()
m = list()
r = 0
s = False

for i in range(0, 9) :
    l = list(map(int, input().split()))
    t.append(l)

    m.append(max(l))

r = max(m)

print(r)

for i in range(0, 9) :
    for j in range(0, 9) :
        if (t[i][j] == r) :
            print(i+1, j+1, end="")
            s = True
            break

    if (s == True) :
        break