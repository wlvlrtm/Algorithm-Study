## 크로아티아 알파벳
import sys

def main() :
    c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    word = sys.stdin.readline().strip()

    for i in c :
        word = word.replace(i, '*')

    print(len(word))



if (__name__ == "__main__") :
    main()