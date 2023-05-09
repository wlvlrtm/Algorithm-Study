## 곱셈
a = int(input())
b = int(input())

b1 = (b % 10)   ## 5
b2 = ((b % 100) // 10)  ## 8
b3 = (b // 100) ## 3


ab1 = (a * b1)  ## 2360
ab2 = (a * b2) * 10  ## 3776 * 10
ab3 = (a * b3) * 100  ## 1416 * 100

print(a * b1)
print(a * b2)
print(a * b3)
print(ab1 + ab2 + ab3)