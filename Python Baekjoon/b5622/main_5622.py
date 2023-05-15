## 다이얼
s = input()
l = [i for i in range(2, 12)]
r = 0

for i in s :
    x = ((ord(i) - 65) // 3) + 3

    if (i == "Z" or i == "S" or i == "Y" or i == "V") :
        x -= 1

    r += x

print(r)