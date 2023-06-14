## 부녀회장이 될테야
t = int(input())
r = list()

for _ in range(0, t) :
    k = int(input())    ## 층
    n = int(input())    ## 호
    f0 = [i for i in range(1, n+1)]  ## 직전 층

    for _ in range(0, k) :
        fn = list()

        for i in range(0, n) :
            fn.append(sum(f0[:i+1]))

        f0 = fn

    r.append(f0[-1])

for j in r :
    print(j)