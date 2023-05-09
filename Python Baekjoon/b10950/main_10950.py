## A + B - 3
t = int(input())

result = list()

for i in range(t) :
    a, b = map(int, input().split())
    re = a + b
    result.append(re)

for j in range(len(result)) :
    print(result[j])