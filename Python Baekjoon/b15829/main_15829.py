## Hashing
l = int(input())
m = 1234567891
r = 31
i = input()
t = 0

for a in range(0, len(i)) :
    t += ((ord(i[a]) - 96) * (r ** a))

print(t % m)