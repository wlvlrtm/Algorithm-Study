"""Find Max num in List"""

from typing import Sequence, Any

def max_of(a: Sequence) -> Any :
  maximum = a[0]

  for i in range(1, len(a)) :
    if (a[i] > maximum) :
      maximum = a[i]

  return maximum


if __name__ == "__main__" :
  num = int(input("배열의 원소 개수를 입력하시오: "))

  x = [None] * num

  for i in range(num) :
    x[i] = int(input(f"원소 x[{i}]의 값을 입력하시오: "))

  print(f"배열 원소의 최대값은 {max_of(x)}입니다.")