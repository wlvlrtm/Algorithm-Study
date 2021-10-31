from Sort.BubbleSort import *
from Sort.ShakerSort import *
from Sort.StraightSelectionSort import *
from Sort.InsertionSort import *
from typing import Any
import copy



class Main :
    def main() -> None :
        """ Main Method """
        
        print("Bubble Sort")
        print("--Original--")
        BubbleSort.Bubble([1, 3, 9, 4, 7, 8, 6])
        print("-----")
        print()
        
        print("--V1--")
        BubbleSort.Bubble1([1, 3, 9, 4, 7, 8, 6])
        print("-----")
        print()

        print("--V2--")
        BubbleSort.Bubble2([1, 3, 9, 4, 7, 8, 6])
        print("-----")
        print()
        print("//////////")
        print()


        print("Shaker Sort")
        print("--Original--")
        ShakerSort.Shaker([9, 1, 3, 4, 6, 7, 8])
        print("-----")
        print()
        print("//////////")
        print()


        print("Selection Sort")
        print("--Original--")
        StraightSelectionSort.Selection([3, 4, 2, 3, 1])
        print("-----")
        print()
        print("//////////")
        print()


        print("Insertion Sort")
        print("--Straight Ver--")
        InsertionSort.StraightInsertion([6, 4, 1, 7, 3, 9, 8])
        print("-----")
        print()

        print("--Binary Ver--")
        InsertionSort.BinaryInsertion([6, 4, 1, 7, 3, 9, 8])
        print("-----")
        print()
        print("//////////")
        print()



        pass








if (__name__ == "__main__") :
    Main.main()		