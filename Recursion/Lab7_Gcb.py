def gcd(x: int, y: int) -> int :
    """ 정수 x와 y 사이의 최대 공약수 반환 """
    ## 22 % 8 = 6
    ## 8 % 6 = 2
    if (y == 0) :
        return x
    else :
        return gcd(y, x % y)    ## 22, 8 -> 8, 6

if __name__ == "__main__" :
    print(gcd(22, 8))
    
