"""Test of Lab3_Max"""

from Lab3_Max import max_of

num = 0
x = []

while True :
  s = input(f"x[{num}]를 입력하시오: ")

  if (s == 'End') :
    break
  x.append(int(s))
  num += 1

print(f"배열 원소의 최댓값은 {max_of(x)}입니다.")