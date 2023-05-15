## 문자열
t = int(input())
l = list()

for i in range(0, t) :
    s = input()
    l.append(s[0]+s[-1])

for j in l :
    print(j)