## 최댓값
x = list()

for i in range(0, 9) :
    x.append(int(input()))

print(max(x), x.index(max(x))+1)