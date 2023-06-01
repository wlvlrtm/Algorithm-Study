## 삼각형과 세 변
a, b, c = 1, 1, 1
r = list()

while (a != 0 and b != 0 and c != 0) :
    a, b, c = map(int, input().split())
    l = [a, b, c]

    if (a + b + c == 0) :
        break

    if (max(l) >= (a+b+c) - max(l)) :
        r.append("Invalid")
    elif (a == b and a == c and b == c) :
        r.append("Equilateral")
    elif (a == b or a == c or b == c) :
        r.append("Isosceles")
    elif (a != b and a != c and b != c) :
        r.append("Scalene")

for i in r :
    print(i)