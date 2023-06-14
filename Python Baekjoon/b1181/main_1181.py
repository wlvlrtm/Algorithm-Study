## 단어 정렬
n = int(input())
l = list()

for _ in range(n) :
    l.append(input())

l = list(set(l))
l.sort()
l.sort(key=len)

for i in l :
    print(i)