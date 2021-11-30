from typing import Any


class Lab7_Factorial :
    """ Cal. Fectorial """
    
    def factorial(n: int) -> int :
        if (n > 0) :
            return n * Lab7_Factorial.factorial(n-1)   ## n! == n * (n - 1)!
        else :
            return 1                    ## (n <= 0)


if (__name__ == "__main__") :
    print(Lab7_Factorial.factorial(3))