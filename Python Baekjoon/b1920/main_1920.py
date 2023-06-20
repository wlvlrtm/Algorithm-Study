## 수 찾기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))

a.sort()

for i in range(m) :
    pl = 0
    pr = n - 1

    while (True) :
        pc = (pl + pr) // 2

        if (a[pc] == l[i]) :
            print(1)
            break
        elif (a[pc] < l[i]) :
            pl = pc + 1
        else :
            pr = pc - 1

        if (pl > pr) :
            print(0)
            break