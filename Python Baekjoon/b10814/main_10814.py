## 나이순 정렬

n = int(input())
l = list()

for _ in range(n) :
    age, name = map(str, input().split())
    age = int(age)
    l.append((age, name))

l.sort(key=lambda x: x[0])

for i in l :
    print(i[0], i[1])