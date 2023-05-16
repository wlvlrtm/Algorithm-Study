## 별 찍기 - 7
n = int(input())
s = 1


for i in range(n, 0, -1) :  ## top
    print(" " * (i - 1), end="")
    print("*" * (s), end="")
    s += 2
    print()

s -= 4

for j in range(1, n) :    ## Bottom
    print(" " * (j), end="")
    print("*" * (s), end="")
    s -= 2

    if (j != n-1) :
        print()