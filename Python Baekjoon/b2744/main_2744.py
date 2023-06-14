## 대소문자 바꾸기
l = input()
r = ""

for i in l :
    if (i.islower()) :
        r += i.upper()
    elif (i.isupper()) :
        r += i.lower()

print(r)