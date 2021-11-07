# 고정 길이 스택 클래스

from typing import Any

class Lab7_Stack :
    """ 고정 길이 스택 클래스 """

    def __init__(self, capacity: int = 256) -> None : ## int capacity = 256
        """ stack 초기화 """
        self.stk = [None] * capacity    ## 스택 본체
        self.capacity = capacity        ## 스택 크기 (용량)
        self.ptr = 0                    ## 스택 포인터 (스택에 쌓인 데이터 개수)
    
  
    def __len__(self) -> int :
        """ stack에 쌓여 있는 데이터 개수 반환 """
        return self.ptr


    def is_empty(self) -> bool :
        """ stack 공백 여부 판단 """
        return self.ptr <= 0
    

    def is_full(self) -> bool :
        """ stack 포화 여부 판단 """
        return self.ptr >= self.capacity ## 스택 포인터 값 (스택에 쌓인 데이터 개수) >= 스택 크기 (스택 용량)


    def push(self, value: Any) -> None :
        """ stack에 데이터를 저장 """
        if (self.is_full()) :           ## 스택이 포화 상태라면,
            raise FixedStack.Full()     ## Full 에러 발생

        self.stk[self.ptr] = value      ## 스택에 데이터 추가
        self.ptr += 1;                  ## 스택 포인터 += 1 (데이터 개수 += 1)
        

    def pop(self) -> Any :
        """ stack에 저장된 데이터 꺼냄 """
        if (self.is_empty()) :          ## 스택이 공백 상태라면,
            raise FixedStack.Empty()    ## Empty 에러 발생
        
        self.ptr -= 1                   ## 스택 포인터 -= 1 (포인터가 최상위 데이터를 가리키도록 변경)

        return self.stk[self.ptr]       ## 꺼낸 데이터 반환


    def pick(self) -> Any :
        """ stack의 최상위 데이터를 반환(삭제 없음) """
        if (self.is_empty()) :          ## 스택이 공백 상태라면,
            raise FixedStack.Empty()    ## Empty 에러 발생

        return self.stk[self.ptr - 1]   ## 최상위 데이터(포인터 값 - 1) 반환


    def find(self, value: Any) -> Any :
        """ stack에서 value에 해당하는 데이터의 인덱스 반환 (없으면 -1 반환) """
        for i in range(self.ptr-1, -1, -1) :    ## 최상위 스택부터 최하위까지 탐색
            if (self.stk[i] == value) :         
                return i                        ## 인덱스 반환

        return -1                               ## 탐색 실패


    def count(self, value: Any) -> bool : 
        """ stack에 있는 value 개수 반환 """
        cnt = 0                             ## value 개수 저장
        for i in range(self.ptr) :          ## 최하위부터 최상위까지 탐색 (선형 검색)
            if (self.stk[i] == value) :     ## 검색 성공
                cnt += 1                    ## 개수 카운트
            
        return cnt


    def __contains__(self, value: Any) -> bool :
        """ stack에 value가 있는지 검사 """
        return self.count(value)


    def dump(self) -> None :
        """ stack의 모든 데이터를 차례로 출력 """
        if (self.is_empty()) :  ## 스택이 비었다면,
            print("Stack is EMPTY.")
        else :
            print(self.stk[:self.ptr])  ## 0 ~ self.ptr-1까지 차례로 출력


    def clear(self) -> None :
        """ stack의 모든 데이터 삭제 """
        self.ptr = 0                    ## 스택 포인터를 0으로 초기화 (스택 덮어쓰기)


    class Empty(Exception) :
        """ 비어 있는 FixedStack에 pop() 또는 Peek()을 호출할 시, 내보내는 예외 처리 """
        pass


    class Full(Exception) :
        """ 가득 찬 FixedStack에 push()를 호출할 시, 내보내는 예외 처리 """
        pass