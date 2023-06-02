## 음계
r = list(map(int, input().split()))

if (r == sorted(r)) :
    print("ascending")
elif (r == sorted(r, reverse=True)) :
    print("descending")
else :
    print("mixed")