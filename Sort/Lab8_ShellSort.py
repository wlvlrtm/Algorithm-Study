from typing import MutableSequence
from typing import Any


class Lab8_ShellSort :
    def Shell(lst: MutableSequence) -> MutableSequence :
        """ Shell Sort Algorithm; Original """
        
        ln = len(lst)   ## Len of List
        h = ln // 2     ## For h-Sort

        while (h > 0) :
            for i in range(h, ln) :
                j = i - h       ## 0 ~ h
                tmp = lst[i]    ## h ~ ln
                
                ## SWAP ##
                while (j >= 0) and (lst[j] > tmp) :   
                    lst[j+h] = lst[j]   ## left <-> right; SWAP
                    j -= h              ## chage the comparison target

                lst[j+h] = tmp          ## input the num into the new Pos.
                ## END SWAP END ##

            h //= 2     ## step Change; 4 -> 2 -> 1

        print(lst)


    def Shell1(lst: MutableSequence) -> MutableSequence :
        """ Shell Sort Algorthm; V1 """

        ln = len(lst)   ## Len of List
        h = 1           ## For h-Sort

        while (h < ln//9) : ## hi = 3 * h(i-1) + 1, h1 = 1
            h = h * 3 + 1

        while (h > 0) :
            for i in range(h, ln) :
                j = i - h       ## 0 ~ h
                tmp = lst[i]    ## h ~ ln
                
                ## SWAP ##
                while (j >= 0) and (lst[j] > tmp) :   
                    lst[j+h] = lst[j]   ## left <-> right; SWAP
                    j -= h              ## chage the comparison target

                lst[j+h] = tmp          ## input the num into the new Pos.
                ## END SWAP END ##

            h //= 3     ## step Change;

        print(lst)


if __name__ == '__main__' :
    num = int(input("Enter the num: "))
    x = [None] * num    ## new arr

    for i in range(num) :
        x[i] = int(input(f'x[{i}]: '))

    print(x)
    Lab8_ShellSort.Shell(x);



