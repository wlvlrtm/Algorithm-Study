## 소수 찾기
import math

num_count = int(input())  # 사용자 입력값; 수의 개수 N
num_list = list(map(int, input().split(' ')))  # 사용자 입력값; N개의 수 (1000 이하 자연수)
natural_num = list(range(2, 1001))  # 리스트 생성 (2 ~ 1000)
count = 0  # 소수의 개수 저장

if (len(num_list) == num_count):  # N개의 수 길이 == 수의 개수 N 검사
    # N보다 작은 합성수 M == sqrt(N)보다 작은 수의 배수; 1000 이하의 합성수 == sqrt(1000)
    for i in range(2, math.ceil(math.sqrt(1000))):
        for j in natural_num:  # j = 2 ~ 1000
            if (j / i == 1):  # j == i (자기 자신)일 경우
                pass  ## pass
            elif (j % i == 0):  # 자기 자신이 아님; 나머지가 없음 == 소수 아님
                natural_num.remove(j)  ## 리스트에서 삭제

for k in num_list:  # k = 사용자가 입력한 N개의 수
    if (k in natural_num):  # 사용자가 입력한 N개의 수 중에 삭제하고 남은 리스트의 요소들이 있는가?
        count += 1  ## 카운트 +1

print(count)  # 결과(소수의 개수) 출력