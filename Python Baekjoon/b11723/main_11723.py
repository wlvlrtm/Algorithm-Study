## 집합
import sys

def main() :
    s = set()
    m = int(sys.stdin.readline().strip())

    for _ in range(m) :
        x = sys.stdin.readline().split()

        if (x[0] == "add") :
            s.add(x[1])
        elif (x[0] == "remove") :
            s.discard(x[1])
        elif (x[0] == "check") :
            if (x[1] in s) :
                print(1)
            else :
                print(0)
        elif (x[0] == "toggle") :
            if (x[1] in s) :
                s.discard(x[1])
            else :
                s.add(x[1])
        elif (x[0] == "all") :
            s = {'4', '7', '18', '15', '9', '3', '10', '20', '17', '16', '6', '1', '8', '5', '11', '19', '13', '12', '14', '2'}
        elif (x[0] == "empty") :
            s = set()



if (__name__ == "__main__") :
    main()