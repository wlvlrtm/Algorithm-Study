from typing import MutableSequence
from typing import Any

class Lab8_InsertionSort :
    def StraightInsertion(lst: MutableSequence) -> MutableSequence :
        """ Straight Insertion Sort Ver """

        ln = len(lst)   # Len. of List

        ## Sort ##
        for i in range(1, ln, 1) :      # (ST: 1, ED: ln-1, SP: 1)
            tmp = i  # First num of UnSorted arr
            ## Pass ##
            for j in range(0, i, 1) :   # (ST: 0, ED: i-1, SP: 1)
                if (lst[tmp] < lst[j]) :    # Swap
                    lst[tmp], lst[j] = lst[j], lst[tmp]
            ## END Pass END ##
            print(lst)
        ## END Sort END ##

        return lst


    def BinaryInsertion(lst: MutableSequence) -> MutableSequence :
        """ Binary Insertion Sort Ver """

        ln = len(lst)   # Len. of List

        ## Sort ##
        for i in range(1, ln, 1) :
            key = lst[i]
            pl = 0      # Left Point; in Sorted Area
            pr = i-1    # Right Point; in Sorted Area

            ## Binary Search in Sorted Area ##
            while True :
                pc = (pl+pr) // 2     # Center Point
                
                if (key == lst[pc]) :   # Search Complite
                    break       
                elif (key > lst[pc]) :  # Move Right
                    pl = pc+1
                else :                  # Move Left
                    pr = pc-1
                
                if (pl > pr) :  # Search end; Input Point Set
                    pd = pr+1
                    break
            ## END Binary Search in Sorted Area END ##

            for j in range(i, pd, -1) :
                lst[j] = lst[j-1]
            lst[pd] = key
            print(lst)
        
        return lst