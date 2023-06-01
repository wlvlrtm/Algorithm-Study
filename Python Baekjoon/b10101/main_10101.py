## 삼각형 외우기
x = int(input())
y = int(input())
z = int(input())

if (x == y == z == 60) :
    print("Equilateral")
elif (x + y + z == 180) :
    if (x == y or x == z or y == z) :
        print("Isosceles")
    elif (x != y and x != z and y != z) :
        print("Scalene")
else :
    print("Error")