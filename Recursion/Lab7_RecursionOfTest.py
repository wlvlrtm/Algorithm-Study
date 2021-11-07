from Stack import FixedStack


def recur(n):
    while (n > 0) :
        recur(n-1)
        print(f"recure({n})")
        n = n-2

recur(4)


def recur2(n) :
    s = FixedStack(n)

    while True :
        if (n > 0) :
            s.push(n)
            n = n-1
            continue
        if not s.is_empty() :
            n = s.pop()
            print(f"recur2({n})")
            n = n-2
            continue
        break

recur2(5)