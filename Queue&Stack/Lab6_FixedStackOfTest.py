from enum import Enum
from Lab6_FixedStack import FixedStack

Menu = Enum('Menu', ['Push', 'Pop', 'Pick', 'Search', 'Dump', 'Exit'])

def selectMenu() -> Menu:
    """ 메뉴 선택 """
    slc = [f'({m.value}){m.name}' for m in Menu]
    
    while True:
        print(*slc, sep = '     ', end="")
        n = int(input(": "))

        if (1 <= n <= len(Menu)) :
            return Menu(n)


s = FixedStack(64)

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = selectMenu()
    
    if (menu == Menu.Push) :
        x = int(input("Input Data: "))
        try: 
            s.push(x)
        except FixedStack.Full:
            print("Stack is Full")

    elif (menu == Menu.Pop) :
        try: 
            x = s.pop()
            print(f"Poped data is {x}.")
        except FixedStack.Empty:
            print("Stack is Empty")

    elif (menu == Menu.Pick) :
        try:
            x = s.pick()
            print(f"Picked data is {x}.")
        except FixedStack.Empty:
            print("Stack is Empty")

    elif (menu == Menu.Search) :
        x = int(input('Search Data Input: '))
        if (x in s):
            print(f"{s.count(x)} data Included, Start Pos is {s.find(x)}.")
        else: 
            print("Search Faild.")

    elif (menu == Menu.Dump) :
        s.dump()

    else:
        break