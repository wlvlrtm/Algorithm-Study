## 알람 시계
hor, min = map(int, input().split())

if (min < 45) :
    x = (min - 45)
    if (hor == 0) :
        hor = 24
    hor -= 1
    min = 60 + x
else :
    min -= 45

print(hor, min)