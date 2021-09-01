l_num = 1
r_num = 7

multi = 1

## Result
count = 1

## User Input
num = int(input())


## cal. result
while (True) :
    if (num == 1) :
        break

    if (l_num < num and num <= r_num) :
        count += 1
        break
    else :
        l_num += (6 * multi)
        r_num += (6 * (multi + 1))
        multi += 1
    count += 1


## print result
print(count)