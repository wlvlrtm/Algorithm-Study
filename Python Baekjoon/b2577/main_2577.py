## 숫자의 개수
import sys

def main() :
    A = int(input())
    B = int(input())
    C = int(input())

    ## A = 150
    ## B = 266
    ## C = 427

    result = A * B * C

    ## result = 17037300

    count = list()

    for i in range(0, 10) :
        count.append(0);

    ## count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while (result != 0) :
        t = (result % 10)
        count[t] += 1
        result = (result // 10)

    for i in range(len(count)) :
        print(count[i])



if (__name__ == "__main__") :
    main()