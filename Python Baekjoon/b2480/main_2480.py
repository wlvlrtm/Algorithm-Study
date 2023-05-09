## 주사위 세개
a, b, c = map(int, input().split())

if (a != b and a != c and b != c) :
    ## 0개
    max = a

    if (max < b):
        max = b

    if (max < c):
        max = c

    print(max * 100)
else :
    if (a == b and a == c and b == c) :
        ## 3개
        print(10000 + a * 1000)
    elif (a == b or a == c and b != c) :
        ## 2개
        print(1000 + a * 100)
    elif (b == c and a != b and a != c) :
        print(1000 + b * 100)