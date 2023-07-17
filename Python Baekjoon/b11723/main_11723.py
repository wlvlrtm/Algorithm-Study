## 집합
import sys

def main() :
    s = set()
    ts = {str(i) for i in range(1, 21)}
    m = int(sys.stdin.readline())

    for _ in range(m) :
        x = sys.stdin.readline().strip().split()

        if (x[0] == "add") :
            s.add(x[1])
        elif (x[0] == "remove") :
            if (x[1] in s) :
                s.remove(x[1])
        elif (x[0] == "check") :
            if (x[1] in s) :
                print(1)
            else :
                print(0)
        elif (x[0] == "toggle") :
            if (x[1] in s) :
                s.remove(x[1])
            else :
                s.add(x[1])
        elif (x[0] == "all") :
            s = ts
        elif (x[0] == "empty") :
            s = set()




if (__name__ == "__main__") :
    main()