from typing import MutableSequence

class Lab8_HeapSort :
    def HeapSort(lsA: MutableSequence) -> None :
        """ Heap Sort """

        def DownHeap(lsA: MutableSequence, left: int, right: int) -> None :
            """ Make a[left] ~ a[right] to the Heap """

            temp = lsA[left]
            parent = left

            ## Make Sub-Tree to Hip ##
            while (parent < (right+1) // 2) :   ## parent = 1 || ((right+1)//2) = (4//2) = 2
                cl = parent * 2 + 1     ## Left node
                cr = parent * 2 + 2     ## Right node

                child = cr if (cr <= right) and (lsA[cr] > lsA[cl]) else cl     ## Choose a Big one
                
                if (temp >= lsA[child]) :
                    break

                lsA[parent] = lsA[child]
                parent = child

            lsA[parent] = temp
            ## END Make Sub-Tree to Hip END ##


        n = len(lsA)

        ## Step 1; Make lsA[i] ~ lsA[n-1] to the Heap ##
        for i in range(((n-1)//2), -1, -1) :
            DownHeap(lsA, i, n-1)
        ## END Step 1; Make lsA[i] ~ lsA[n-1] to the Heap END ##

        ## Step 2; lsA[0] <-> lsA[i] ##
        for i in range(n-1, 0, -1) :
            lsA[0], lsA[i] = lsA[i], lsA[0] ## SWAP
            DownHeap(lsA, 0, i-1)           ## Make Heap
        ## END Step 2; lsA[0] <-> lsA[i] END ##

        print(lsA)



if __name__ == "__main__" :
    lsA = [1, 3, 12, 6, 4, 11, 8, 7, 3, 2, 6, 5]
    Lab8_HeapSort.HeapSort(lsA)