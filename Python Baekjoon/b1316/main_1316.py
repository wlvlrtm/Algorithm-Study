## 그룹 단어 체커
import sys

def main() :
    n = int(sys.stdin.readline().strip())
    cnt = n

    for i in range(n) :
        word = sys.stdin.readline().strip()

        for j in range(len(word) - 1) :
            if word[j] == word[j + 1] :
                pass
            elif (word[j] in word[j + 1 : ]) :
                cnt -= 1
                break

    print(cnt)


if (__name__ == "__main__") :
    main()