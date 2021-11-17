from typing import MutableSequence
from Lab8_QuickSort_Stack import Stack


class Lab8_QuickSort :
    def InsertionSort(a: MutableSequence, left: int, right: int) -> None :
        """ Insertion Sort; FOR Qsort2 """

        for i in range(left+1, right+1) :
            j = i
            tmp = a[i]
            
            while (j > 0) and (a[j-1] > tmp) :
                a[j] = a[j-1]
                j -= 1

            a[j] = tmp


    def Partition(a: MutableSequence) -> None :
        """ print the split of array a """

        n = len(a)      ## Len of arr
        pl = 0          ## left pointer
        pr = n-1        ## right pointer
        x = a[n//2]     ## pivot

        while (pl <= pr) :
            while (a[pl] < x) :
                pl += 1
            while (a[pr] > x) :
                pr -= 1

            ## SWAP ##
            if (pl <= pr) :
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
            ## END SWAP END ##

        print(f"Pivot: {x}")
        
        print(f"a[0] ~ a[pl-1]: ", end="")
        print(*a[0 : pl])

        if (pl > pr+1) :
            print(f"a[pr+1] ~ a[pl-1]: ")
            print(*a[pr+1 : pl])

        print(f"a[pr+1] ~ a[n-1]: ", end="")
        print(*a[pr+1 : n])


    def Qsort(a: MutableSequence, left: int, right: int) -> None :
        """ Quick Sort; Original Ver """

        pl = left       ## Left Point
        pr = right      ## Right Point
        x = a[(left + right) // 2]  ## Pivot

        print(f"a[{left}] ~ a[{right}]: ", *a[left : right + 1])

        while (pl <= pr) :
            while (a[pl] < x) :
                pl += 1
            while (a[pr] > x) :
                pr -= 1

            ## SWAP ##
            if (pl <= pr) :
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
            ## END SWAP END ##

        if (left < pr) :
            Lab8_QuickSort.Qsort(a, left, pr)
        if (pl < right) :
            Lab8_QuickSort.Qsort(a, pl, right)


    def Qsort1(a: MutableSequence, left:int, right: int) -> None :
        """ Quick Sort; Non-Recur Ver """

        range = Stack(right - left + 1)

        range.push((left, right))

        while not range.is_empty() :
            pl, pr = left, right = range.pop()
            x = a[(left + right) // 2]  ## Pivot

            while (pl <= pr) :
                while (a[pl] < x) :
                    pl += 1
                while (a[pr] > x) :
                    pr -= 1

                ## SWAP ##
                if (pl <= pr) :
                    a[pl], a[pr] = a[pr], a[pl]
                    pl += 1
                    pr -= 1
                ## END SWAP END ##

        if (left < pr) :
            range.push((left, pr))
        if (pl < right) :
            range.push((pl, right))


    def Qsort2(a: MutableSequence, left: int, right: int) -> None :
        """ Quick Sort; Quick Sort + Insertion Sort Ver """

        def Sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int) :
            if (a[idx2] < a[idx1]) :
                a[idx2], a[idx1] = a[idx1], a[idx2]
            if (a[idx3] < a[idx2]) :
                a[idx3], a[idx2] = a[idx2], a[idx3]
            if (a[idx2] < a[idx1]) :
                a[idx2], a[idx1] = a[idx1], a[idx2]
            return idx

        if (right - left) < 9 :
            Lab8_QuickSort.InsertionSort(a, left, right)
            

        pl = left       ## Left Point
        pr = right      ## Right Point
        x = a[(left + right) // 2]  ## Pivot

        print(f"a[{left}] ~ a[{right}]: ", *a[left : right + 1])

        while (pl <= pr) :
            while (a[pl] < x) :
                pl += 1
            while (a[pr] > x) :
                pr -= 1

            ## SWAP ##
            if (pl <= pr) :
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
            ## END SWAP END ##

        if (left < pr) :
            Lab8_QuickSort.Qsort(a, left, pr)
        if (pl < right) :
            Lab8_QuickSort.Qsort(a, pl, right)




if __name__ == "__main__" :

    x = [8, 7, 4, 3, 1, 2, 5, 9, 6]
    Lab8_QuickSort.Partition(x)
    print()
    
    Lab8_QuickSort.Qsort(x, 0, len(x)-1)
    print(f"Sorted: {x}")
    print()

    x1 = [8, 7, 65, 4, 0, 9, 1]
    Lab8_QuickSort.Qsort1(x1, 0, len(x1)-1)
    print(f"Sorted: {x1}")
    print()

    x2 = [5, 6, 1, 3, 20, 0, 6, 2, 7]
    Lab8_QuickSort.Qsort2(x2, 0, len(x2)-1)
    print(f"Sorted: {x2}")
    print()
