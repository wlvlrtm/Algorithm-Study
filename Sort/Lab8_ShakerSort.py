from typing import MutableSequence
from typing import Any



class Lab8_ShakerSort :
    def Shaker(lst: MutableSequence) -> MutableSequence :
        """ Shaker Sort Original """

        left: int = 0                 # Left Point
        right: int = len(lst)-1       # Right Point
        last: int = right             # Scan Last Index

        cnt: int = 0            # Comparison Count
        snt: int = 0            # Swap Count
        psn: int = 1            # Pass Count
        isExchng: bool = False  # Is Exchange?

        ## Sorting ##
        while (left < right) :
            print(f"PASS {psn}")
            isExchng = False        # Exchanged Check Reset

            ## right2left Pass ##
            for i in range(right, left, -1) :   # (ST: right, ED: left, SP: -1)
                ## Comparison Process Print 1 ##
                cnt += 1    # Comparison Count += 1
                for j in range(0, len(lst)-1, 1) :  # (ST: 0, ED: len(lst)-2, SP: 1)
                    print(f"{lst[j]:2}" + ("  " if (j != i-1) else (" -" if (lst[j+1] > lst[j]) else " +")), end="")
                print(f"{lst[len(lst)-1]:2}")
                ## END Comparison Process Print 1 END ##

                ## Swap ##
                if (lst[i-1] > lst[i]) :
                    lst[i-1], lst[i] = lst[i], lst[i-1]
                    snt += 1        # Swap Count += 1
                    last = i        # Pass End(left) Point Update
                    isExchng = True # Exchanged Check
                ## END Swap END ##
            ## END right2left Pass END ##

            left = last
            psn += 1

            ## Comparison Process Print 2 ##
            for j in range(0, len(lst)-1, 1) :
                print(f"{lst[j]:2}" + "  ", end="")
            print(f"{lst[len(lst)-1]:2}")
            print()
            ## END Comparison process Print 2 END ##

            ## Exchange Bool Check ##
            if (isExchng == False) :
                break
            ## END Exchange Bool Check END ##


            ## -- !! -- ##


            print(f"PASS {psn}")
            isExchng = False        # Exchanged Check Reset

            ## left2right Pass ##
            for i in range(left, right, 1) :   # (ST: left, ED: right, SP: 1)
                ## Comparison Process Print 1 ##
                cnt += 1    # Comparison Count += 1
                for j in range(0, len(lst)-1, 1) :  # (ST: 0, ED: len(lst)-2, SP: 1)
                    print(f"{lst[j]:2}" + ("  " if (j != i) else (" +" if (lst[j] > lst[j+1]) else " -")), end="")
                print(f"{lst[len(lst)-1]:2}")
                ## END Comparison Process Print 1 END ##

                ## Swap ##
                if (lst[i+1] < lst[i]) :
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    snt += 1        # Swap Count += 1
                    last = i        # Pass End(left) Point Update
                    isExchng = True # Exchanged Check
                ## END Swap END ##
            ## END right2left Pass END ##

            right = last
            psn += 1

            ## Comparison Process Print 2 ##
            for j in range(0, len(lst)-1, 1) :
                print(f"{lst[j]:2}" + "  ", end="")
            print(f"{lst[len(lst)-1]:2}")
            print()
            ## END Comparison process Print 2 END ##

            ## Exchange Bool Check ##
            if (isExchng == False) :
                break
            ## END Exchange Bool Check END ##
        ## END Sorting END ##

