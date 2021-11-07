"""List $$ Tuple Control Exercise 2"""

import copy


lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
lst1 = lst2
lst1[1] = 999
print(lst1)
print(lst2)


lst1 = [1, 2, 3, 4, 5]
lst2 = lst1
print(lst1 is lst2)
lst1[2] = 9
print(lst1)
print(lst2)


x = ["A", "B", "C", "D"]

for i in range(len(x)) :
  print(f"x[{i}] = {x[i]}")
print("")
for i, name in enumerate(x) :
  print(f"x[{i}] = {name}")


def change(lst, idx, val) :
  lst[idx] = val

x = [11, 22, 33, 44, 55]
print("x = ", x)

index = int(input("업데이트할 인덱스: "))
value = int(input("새로운 값: "))

change(x, index, value)
print(f"x = {x}")


x = [1, 2, 3, 5.6, [88, 99], "ABC"]

for i in range(len(x)) :
  print(f"x[{i}] = {x[i]}")


x = [[1, 2, 3], [4, 5, 6]]

y = x.copy()

x[0][1] = 9

print(x)
print(y)


x = [[1, 2, 3], [4, 5, 6]]

y = copy.deepcopy(x)

x[0][1] = 9

print(x)
print(y)