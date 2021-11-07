def factorial(n: int) -> int:
    """ 양의 정수 n의 팩토리얼 값을 재귀함수로 계산 """
    if (n > 0) :
        return n * factorial(n - 1)
    else :
        return 1

if __name__ == "__main__" :
    print(factorial(3))