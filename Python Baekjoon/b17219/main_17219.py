## 비밀번호 찾기
import sys

def main() :
    n, m = map(int, sys.stdin.readline().split())
    note = dict()
    result = list()

    for _ in range(n) : ## pwd save
        add, pwd = map(str, sys.stdin.readline().split())
        note[add] = pwd
        note[pwd] = add

    for _ in range(m) : ## pwd search
        ans = sys.stdin.readline().strip()
        result.append(note[ans])

    for i in result :
        print(i)



if (__name__ == "__main__") :
    main()