from typing import MutableSequence
from typing import Any


class Lab8_BubbleSort :
    def Bubble(lst: MutableSequence) -> MutableSequence :
        """ Bubble Sort Algorithm; Original """
        
        ln: int = len(lst)      ## Len of List    
        cnt: int = 0            ## Comparison Count
        snt: int = 0            ## Swap Count

        ## Sorting ##
        for i in range(0, ln-1, 1) :    ## (ST: 0, ED: ln-2, SP: 1)
            ## Pass ##
            print(f"PASS {i+1}")
            for j in range(ln-1, i, -1) :  ## (ST: ln-1, ED: i+1, SP: -1)

                ## Comparison Process Print 1 ##
                cnt += 1    ## Comparison Count += 1
                for k in range(0, ln-1, 1) : ## (ST: 0, ED: ln-2, SP: 1)
                    print(f"{lst[k]:2}" + ("  " if (k != j-1) else (" +" if (lst[j-1] > lst[j]) else " -")), end="")
                print(f"{lst[ln-1]:2}")
                ## END Comparison Process Print 1 END ##

                ## Swap ##
                if (lst[j-1] > lst[j]) :    
                    lst[j-1], lst[j] = lst[j], lst[j-1]
                    snt += 1    ## Swap Count += 1
                ## END Swap END ##
            ## END Pass END ##

            ## Comparison Process Print 2 ##
            for k in range(0, ln-1, 1) : ## (ST: 0, ED: ln-2, SP: 1)
                print(f"{lst[k]:2}" + "  ", end="")
            print(f"{lst[ln-1]:2}")
            print()
            ## END Comparison Process Print 2 END ##
        ## END Sorting END ##

        print()
        print(f"Comparison Count: {cnt}")
        print(f"Swap Count: {snt}")
        print()

        return lst
        

    def Bubble1(lst: MutableSequence) -> MutableSequence :
        """ Bubble Sort Algorthm V1 """

        ln: int = len(lst)      # Len of List    
        cnt: int = 0            # Comparison Count
        snt: int = 0            # Swap Count
        isExchng: bool = False  # Is Exchange?

        ## Sorting ##
        for i in range(0, ln-1, 1) :    # (ST: 0, ED: ln-2, SP: 1)
            ## Pass ##
            print(f"PASS {i+1}")
            isExchng = False        # Exchanged Check Reset
            for j in range(ln-1, i, -1) :  # (ST: ln-1, ED: i+1, SP: -1)
                ## Comparison Process Print 1 ##
                cnt += 1    # Comparison Count += 1
                for k in range(0, ln-1, 1) : # (ST: 0, ED: ln-2, SP: 1)
                    print(f"{lst[k]:2}" + ("  " if (k != j-1) else (" +" if (lst[j-1] > lst[j]) else " -")), end="")
                print(f"{lst[ln-1]:2}")
                ## END Comparison Process Print 1 END ##

                ## Swap ##
                if (lst[j-1] > lst[j]) :    
                    lst[j-1], lst[j] = lst[j], lst[j-1]
                    snt += 1        # Swap Count += 1
                    isExchng = True # Exchanged Check
                ## END Swap END ##
            ## END Pass END ##

            ## Comparison Process Print 2 ##
            for k in range(0, ln-1, 1) : # (ST: 0, ED: ln-2, SP: 1)
                print(f"{lst[k]:2}" + "  ", end="")
            print(f"{lst[ln-1]:2}")
            print()
            ## END Comparison Process Print 2 END ##

            ## Exchange Bool Check; False -> Sorting STOP ##
            if (isExchng == False) :
                break
            ## END Exchange Bool Check END ##
        ## END Sorting END ##

        print()
        print(f"Comparison Count: {cnt}")
        print(f"Swap Count: {snt}")
        print()

        return lst


    def Bubble2(lst: MutableSequence) -> MutableSequence :
        """ Bubble Sort Algorthm V2 """

        ln: int = len(lst)      # Len of List    
        cnt: int = 0            # Comparison Count
        snt: int = 0            # Swap Count
        end: int = 0            # Last Com. index
        psn: int = 1            # Pass Count
        isExchng: bool = False  # Is Exchange?

        ## Sorting ##
        while (end < ln-1) :    # (ST: end, ED: ln-2, SP: 1)
            print(f"PASS {psn}")
            isExchng = False        # Exchanged Check Reset
            
            ## Pass ##
            for j in range(ln-1, end, -1) :  # (ST: ln-1, ED: end, SP: -1)
                ## Comparison Process Print 1 ##
                cnt += 1    # Comparison Count += 1
                for k in range(0, ln-1, 1) : # (ST: 0, ED: ln-2, SP: 1)
                    print(f"{lst[k]:2}" + ("  " if (k != j-1) else (" +" if (lst[j-1] > lst[j]) else " -")), end="")
                print(f"{lst[ln-1]:2}")
                ## END Comparison Process Print 1 END ##

                ## Swap ##
                if (lst[j-1] > lst[j]) :    
                    lst[j-1], lst[j] = lst[j], lst[j-1]
                    snt += 1        # Swap Count += 1
                    end = j         # Last Com. index Update
                    isExchng = True # Exchanged Check
                ## END Swap END ##
            ## END Pass END ##
            
            psn += 1

            ## Comparison Process Print 2 ##
            for k in range(0, ln-1, 1) : # (ST: 0, ED: ln-2, SP: 1)
                print(f"{lst[k]:2}" + "  ", end="")
            print(f"{lst[ln-1]:2}")
            print()
            ## END Comparison Process Print 2 END ##

            ## Exchange Bool Check; False -> Sorting STOP ##
            if (isExchng == False) :
                break
            ## END Exchange Bool Check END ##
        ## END Sorting END ##

        print()
        print(f"Comparison Count: {cnt}")
        print(f"Swap Count: {snt}")
        print()

        return lst