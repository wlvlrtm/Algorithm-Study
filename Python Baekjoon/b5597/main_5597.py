## 과제 안 내신 분..?
l = list()

for i in range(0, 30) :
    l.append(i+1)

for j in range(0, 28) :
    n = int(input())
    l.remove(n)

for k in l :
    print(k)