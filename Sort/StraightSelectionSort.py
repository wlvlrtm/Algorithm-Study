from typing import MutableSequence
from typing import Any

class StraightSelectionSort :
    def Selection(lst: MutableSequence) -> MutableSequence :
        """ StraightSelectionSort Original """

        print(f"BEFOR: {lst}")

        ln = len(lst)   # Len of List

        ## Sort ##
        for i in range(0, ln-1, 1) :  # (ST: 0, ED: ln-2, SP: 1)
            min = i

            ## min Searching ##
            for j in range(i+1, ln, 1) :     # (ST: i+1, ED: ln-1, SP: 1)
                if (lst[min] > lst[j]) :
                    min = j     # min change
            ## END min Searching END ##

            lst[min], lst[i] = lst[i], lst[min]     # Swap
            print(lst)
        ## END Sort END ##


        print(f"AFTER: {lst}")

        return lst
            
