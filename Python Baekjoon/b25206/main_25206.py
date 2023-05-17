## 너의 평점은
rc = 0
rs = 0

for i in range(0, 20) :
    n, s, c = map(str, input().split())
    p = 0
    s = float(s)

    if (c == "A+") :
        p = 4.5
    elif (c == "A0") :
        p = 4.0
    elif (c == "B+") :
        p = 3.5
    elif (c == "B0") :
        p = 3.0
    elif (c == "C+") :
        p = 2.5
    elif (c == "C0") :
        p = 2.0
    elif (c == "D+") :
        p = 1.5
    elif (c == "D0") :
        p = 1.0
    elif (c == "F") :
        p = 0.0
    elif (c == "P") :
        continue

    rc += (s * p)
    rs += s

print("%.6f" %(rc / rs))