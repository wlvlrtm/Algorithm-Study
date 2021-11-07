from Lab5_SearchWhile import Seq_Search

if __name__ == '__main__' :
  print("실수를 검색합니다.")
  print("'End'를 입력하면 종료합니다.")

  num = 0
  x = []

  while True:
    s = input(f'x[{num}]')
    if s == 'End':
      break
    x.append(float(s))
    num += 1

  key = float(input("검색할 값 입력: "))
  idx = Seq_Search(x, key)

  if (idx == -1) :
    print("값 없음")
  else :
    print(f"검색된 값: x[{idx}]에 있음")