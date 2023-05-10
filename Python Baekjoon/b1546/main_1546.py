## 평균
n = int(input())

score_list = list(map(int,input().split()))

M = 0
add_all = 0

for i in range(n) :
    if (M < score_list[i]) :
        M = score_list[i]

for i in range(len(score_list)) :
    score_list[i] =  score_list[i] / M * 100
    add_all += score_list[i]

print(add_all / len(score_list))