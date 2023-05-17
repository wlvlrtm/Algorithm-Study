## 팰린드롬인지 확인하기
s = input()
n = (len(s) // 2)
r = 1

for i in range(0, n) :
    if (s[i] == s[-(i+1)]) :
        r = 1
        continue
    else :
        r = 0
        break

print(r)