## 블랙잭
N, M = map(int,input().split())

Card = list(map(int,input().split()))
result = 0

## Card = [5, 6, 7, 8, 9]

for i in range(N) : ## 5 (0 ~ 4)
    for j in range(i+1, N) :
        for q in range(j+1, N) :
            add = Card[i] + Card[j] + Card[q]
            if (add > M) :
                continue
            else :
                result = max(result, add)

print(result)