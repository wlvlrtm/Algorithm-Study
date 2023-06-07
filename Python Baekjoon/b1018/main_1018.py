## 체스판 다시 칠하기
n, m = map(int, input().split())
b, r = list(), list()

for _ in range(n) :
    b.append(input())

for i in range(n - 7) :
    for j in range(m - 7) :
        dw, db = 0, 0

        for k in range(i, i + 8) :
            for l in range(j, j + 8) :
                if ((k + l) % 2 == 0) :
                    if (b[k][l] != "B") :
                        dw += 1
                    if (b[k][l] != "W") :
                        db += 1
                else :
                    if (b[k][l] != "W") :
                        dw += 1
                    if (b[k][l] != "B") :
                        db += 1

        r.append(dw)
        r.append(db)

print(min(r))