class Lab1_Maxx :
    def Maxx() -> None :
        """Find Max num of a, b, c"""
        
        ## 3 num Input ##
        print("세 정수를 입력하시오")
        
        a = int(input("정수 a를 입력하세요 > "))
        b = int(input("정수 b를 입력하세요 > "))
        c = int(input("정수 c를 입력하세요 > "))
        
        ## END 3 num Input END ##

        max = a     # Max num Initialize
        
        ## Find Max num ##
        if (b > max) :
            max = b
        if (c > max) :
            max = c
        ## END Find Max num END ##

        print(f"최댓값은 {max}입니다.")    # return Max