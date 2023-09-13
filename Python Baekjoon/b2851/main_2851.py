## 슈퍼 마리오
num = list()
result = 0

## 0 ~ 9 까지의 리스트(num)에 버섯 점수 추가
for i in range(10) :
    num.append(int(input()))

for i in num :  ## 변수 i == num 리스트 값
    result += i  ## result 변수에 i(num 리스트 값)를 하나씩 더해 저장

    if (result == 100) :  ## result가 100이면,
        break  ## for 문 탈출
    elif (result > 100) :  ## result가 100보다 크면,
        if (abs(result - 100) > abs(result - i - 100)) :  ## 100보다 작은 수와 큰 수 중에서 더 100에 가까운 수 찾기
            result -= i
            break

print(result)  ## 결과 출력