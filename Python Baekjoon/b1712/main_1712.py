## 손익분기점
import sys

def main() :
    cost_A, cost_B, cost_C = map(int, sys.stdin.readline().split())

    if (cost_C <= cost_B) :
        print(-1)
    else :
        num = (cost_A // (cost_C - cost_B))
        print(num + 1)



if (__name__ == "__main__") :
    main()