## 선형 검색 알고리즘; While

from typing import Sequence, Any

def Seq_Search(a: Sequence, key: Any) -> int:
  i = 0

  while True :
    if i == len(a) :
      return -1
    elif a[i] == key:
      return i
    i += 1