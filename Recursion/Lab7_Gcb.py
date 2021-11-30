from typing import Any


class Lab7_Gcb :
    """ GCB Cal."""

    def Gcb(x: int, y: int) -> int :
        if (y == 0) :
            return x
        else :
            return Lab7_Gcb.Gcb(y, x % y)



if (__name__ == "__main__") :
    print(Lab7_Gcb.Gcb(22, 8))