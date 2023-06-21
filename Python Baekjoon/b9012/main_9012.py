t = int(input())

for i in range(t) :
    s = list()
    x = input()

    for j in x :
        if (j == "(") :
            s.append(j)
        elif (j == ")") :
            if (not s) :
                print("NO")
                break
            s.pop()
    else :
        if not s :
            print("YES")
        else :
            print("NO")