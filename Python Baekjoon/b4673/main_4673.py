## 셀프 넘버
def main() :
    num = [False] * 10000

    for i in range(1, len(num) + 1) :
        x = sum(i)

        if (x < len(num)) :
            num[x] = True

    for j in range(1, len(num)) :
        if not (num[j]) :
            print(j)

def sum(n) :
    t = 0
    t += n

    while (n != 0) :
        t += (n % 10)
        n = (n // 10)

    return t



if (__name__ == "__main__") :
    main()