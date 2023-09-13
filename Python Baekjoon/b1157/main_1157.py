## 단어 공부
import sys

def main() :
    words = sys.stdin.readline().strip().upper()

    u_words = list(set(words))
    cnt = []

    for i in u_words :
        num = words.count(i)
        cnt.append(num)

    if (cnt.count(max(cnt)) > 1) :
        print('?')
    else :
        mxx = cnt.index(max(cnt))
        print(u_words[mxx])



if (__name__ == "__main__") :
    main()