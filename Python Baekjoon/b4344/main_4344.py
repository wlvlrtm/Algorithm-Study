## 평균은 넘겠지
C = int(input())    ## 테스트 케이스 개수
aver = 0        ## 평균
percent_list = list()   ## 평균 이상 비율 계산값 리스트

while (C > 0) :
    add_all = 0     ## 점수 합산
    over_num = 0    ## 평균 초과 학생 수
    n = list(map(int,input().split()))  ## 학생들 점수 입력

    for i in range(1, len(n)) :
        add_all += n[i]     ## 점수 전체 합산

    aver = (add_all / (len(n) - 1))     ## 평균 계산

    for a in range(1, len(n)) :
        if (aver < n[a]) :     ## 평균 이상 학생 검사
            over_num += 1

    ## 평균 이상 비율 계산값; 리스트에 추가
    percent = (over_num / (len(n) - 1)) * 100
    percent_list.append(percent)
    C -= 1

## 결과 출력
for x in range(len(percent_list)) :
    print("%0.3f%%" %(percent_list[x]))