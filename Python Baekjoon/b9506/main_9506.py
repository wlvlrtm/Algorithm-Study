## 약수들의 합
while(True) :
    l = 0
    x = list()
    n = int(input())

    if (n == -1) :
        break

    for i in range(1, n) :
        if (n % i == 0) :
            l += i
            x.append(i)

    if (l == n) :
        print(f"{n} =", end="")

        for j in x :
            print(f" {j}", end="")

            if (j != x[len(x)-1]) :
                print(" +", end="")
        print()
    else :
        print(f"{n} is NOT perfect.")