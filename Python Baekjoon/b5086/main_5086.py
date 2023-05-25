## 배수와 약수
r = list()

while(True) :
    a, b = map(int, input().split())

    if (a == 0 and b == 0) :
        break

    if (b % a == 0) :  ## 1
        r.append("factor")
    elif (a % b == 0) :    ## 2
        r.append("multiple")
    else :  ## 3
        r.append("neither")

for i in r :
    print(i)