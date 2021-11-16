from typing import Any
from typing import Sequence, MutableSequence

class Lab8_MergeSort :
    def MergeSortedList(lsA: Sequence, lsB: Sequence, lsC: MutableSequence) -> None :
        """ lsA + lsB -> lstC; MERGE ONLY """

        pA, pB, pC = 0, 0, 0                           ## pointer of lsA, lsB, lsC
        lnA, lnB, lnC = len(lsA), len(lsB), len(lsC)   ## len of lsA, lsB, lsC

        ## lsA, lsB Combine ##
        while (pA < lnA) and (pB < lnB) :
            if (lsA[pA] <= lsB[pB]) :
                lsC[pC] = lsA[pA]
                pA +=1
            else :
                lsC[pC] = lsB[pB]
                pB += 1
            pC += 1
            
        while (pA < lnA) :   ## Add to lsC that Remain num of lsA
            lsC[pC] = lsA[pA]
            pA, pC = pA+1, pC+1

        while (pB < lnB) :   ## Add to lsC that Remain num of lsB
            lsC[pC] = lsB[pB]
            pB, pC = pB+1, pC+1
        ## END lsA, lsB Combine END ##


    def MergeSort(lsA: MutableSequence) -> None :
        """ Merge Sort; Original Ver """

        def _MergeSort(lsA: MutableSequence, left: int, right: int) -> None :
            """ a[left] ~ a[right]; Recursion """

            if (left < right) :
                center = (left + right) // 2

                _MergeSort(lsA, left, center)       ## 0 ~ center
                _MergeSort(lsA, center+1, right)    ## center+1 ~ right

                p = j = 0
                i = k = left

                ## LEFT, RIGHT Merge ##
                ## Left of lsA Copy to buff ##
                while (i <= center) :   
                    buff[p] = lsA[i]
                    p += 1
                    i += 1
                ## END Left of lsA Copy to buff END ##

                ## Right of lsA Copy to buff ##
                while (i <= right) and (j < p) :
                    if (buff[j] <= lsA[i]) :
                        lsA[k] = buff[j]
                        j += 1
                    else :
                        lsA[k] = lsA[i]
                        i += 1
                    k += 1
                ## END Right of lsA Copy to buff ##

                ## Add the rest nums ##
                while (j < p) :
                    lsA[k] = buff[j]
                    k += 1
                    j += 1
                ## END Add the rest nums END ##
                ## END LEFT, RIGHT Merge END ##
        
        ln = len(lsA)
        buff = [None] * ln          ## Arr for Merge
        _MergeSort(lsA, 0, ln-1)    ## merge Sort Call
        print(lsA)
            

if __name__ == "__main__" :
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a)+len(b))

    Lab8_MergeSort.MergeSortedList(a, b, c)

    print("a: ", a)
    print("b: ", b) 
    print("c: ", c)

    lsA = [1, 3, 12, 6, 4, 11, 8, 7, 3, 2, 6, 5]
    Lab8_MergeSort.MergeSort(lsA)