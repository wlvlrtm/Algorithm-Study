## 나머지
A = list()
B = 42

left = set()

for i in range(0, 10) :
    A.append(int(input()))
    left.add(A[i] % B)

list_left = list(left)

print(len(list_left))