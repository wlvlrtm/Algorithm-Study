## OX퀴즈
n = int(input())  ## 테스트 케이스 개수

result_list = list()  ## 스코어 저장 리스트

## O, X 답안 리스트 생성
for i in range(n) :
    combo = 0  ## 연속 정답 포인트
    result = 0  ## 최종 스코어

    St = input()  ## 답안 입력
    XO_list = list(St)  ## 리스트 저장

    ## O 연속 개수 검사
    for a in range(len(XO_list)) :
        ## 콤보 계산
        if (XO_list[a] == 'O') :
            combo += 1
        else :  ## 오답 시, 콤보 초기화
            combo = 0

        result += combo  ## 최종 콤보 포인트 합산
    result_list.append(result)  ## 스코어 저장 리스트 추가

## 결과 출력
for x in range(len(result_list)) :
    print(result_list[x])