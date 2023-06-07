## ACM 호텔
t = int(input())
r = list()

for i in range(0, t) :
    h, w, n = map(int, input().split())
    v = 0
    arr = list()

    for j in range(0, w) :
        v += 1

        for k in range(0, h) :
            v += 100
            arr.append(v)

        v = j + 1

    r.append(arr[n-1])

for l in r :
    print(l)