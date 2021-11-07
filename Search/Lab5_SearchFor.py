## List Search; for
from typing import Sequence, Any

def Seq_Search(a: Sequence, key: Any) -> int:
  for i in range(len(a)) :  ## i = 0 ~ 6; +1
    if (a[i] == key) :
      return i
  return -1