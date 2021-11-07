import import_ipynb
from Lab5_BiSearch import bin_search

a = list()

while True:
  num = input("원소 입력 (중단: End): ")
  
  if (num == "End") :
    break
  else :
    a.append((int(num)))


i = int(input("검색할 값: "))
print(f"검색값 위치: a[{bin_search(a, i)}]")