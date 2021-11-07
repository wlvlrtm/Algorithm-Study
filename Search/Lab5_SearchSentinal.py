from typing import Any, Sequence
import copy


def Seq_Search(seq: Sequence, key: Any) -> int:
  a = copy.deepcopy(seq)
  a.append(key)

  i = 0
  while True :
    if (a[i] == key) :
      break
    i += 1
  return -1 if (i == len(seq)) else i 