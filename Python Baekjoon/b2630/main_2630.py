## 색종이 만들기
import sys

global white, blue, paper

def main() :
    global white, blue, paper

    n = int(sys.stdin.readline().strip())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    white, blue = 0, 0
    cut(0,0, n)

    print(white)
    print(blue)

def cut(x, y, n) :
    global white, blue, paper

    color = paper[x][y]

    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if (color != paper[i][j]) :
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return

    if (color == 0) :
        white += 1
    elif (color == 1) :
        blue += 1



if (__name__ == "__main__") :
    main()